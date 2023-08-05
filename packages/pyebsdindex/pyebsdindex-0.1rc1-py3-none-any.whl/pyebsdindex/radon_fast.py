"""This software was developed by employees of the US Naval Research Laboratory (NRL), an
agency of the Federal Government. Pursuant to title 17 section 105 of the United States
Code, works of NRL employees are not subject to copyright protection, and this software
is in the public domain. PyEBSDIndex is an experimental system. NRL assumes no
responsibility whatsoever for its use by other parties, and makes no guarantees,
expressed or implied, about its quality, reliability, or any other characteristic. We
would appreciate acknowledgment if the software is used. To the extent that NRL may hold
copyright in countries other than the United States, you are hereby granted the
non-exclusive irrevocable and unconditional right to print, publish, prepare derivative
works and distribute this software, in any medium, or authorize others to do so on your
behalf, on a royalty-free basis throughout the world. You may improve, modify, and
create derivative works of the software or any portion of the software, and you may copy
and distribute such modifications or works. Modified works should carry a notice stating
that you changed the software and should note the date and nature of any such change.
Please explicitly acknowledge the US Naval Research Laboratory as the original source.
This software can be redistributed and/or modified freely provided that any derivative
works bear some notice that they are derived from it, and any modified versions bear
some notice that they have been modified.

Author: David Rowenhorst;
The US Naval Research Laboratory Date: 21 Aug 2020"""

from os import environ
from timeit import default_timer as timer

from numba import jit, prange
import numpy as np

RADDEG = 180.0/np.pi
DEGRAD = np.pi/180.0



class Radon:
  def __init__(self, image=None, imageDim=None, nTheta=180, nRho=90, rhoMax=None):
    self.nTheta = nTheta
    self.nRho = nRho
    self.rhoMax = rhoMax
    self.indexPlan = None
    if (image is None) and (imageDim is None):
      self.theta = None
      self.rho = None
      self.imDim = None
    else:
      if image is not None:
        self.imDim = np.asarray(image.shape[-2:])
      else:
        self.imDim = np.asarray(imageDim[-2:])
      self.radon_plan_setup(imageDim=self.imDim, nTheta=self.nTheta, nRho=self.nRho, rhoMax=self.rhoMax)

  def radon_plan_setup(self, image=None, imageDim=None, nTheta=None, nRho=None, rhoMax=None):
    if (image is None) and (imageDim is not None):
      imDim = np.asarray(imageDim, dtype=np.int64)
    elif (image is not None):
      imDim =  np.shape(image)[-2:] # this will catch if someone sends in a [1 x N x M] image
    else:
      return -1
    imDim = np.asarray(imDim)
    self.imDim = imDim
    if (nTheta is not None) : self.nTheta = nTheta
    if (nRho is not None): self.nRho = nRho
    self.rhoMax = rhoMax if (rhoMax is not None) else np.round(np.linalg.norm(imDim)*0.5)

    deltaRho = float(2 * self.rhoMax) / (self.nRho)
    self.theta = np.arange(self.nTheta, dtype = np.float32)*180.0/self.nTheta
    self.rho = np.arange(self.nRho, dtype = np.float32)*deltaRho - (self.rhoMax-deltaRho)

    #xmin = -1.0*(self.imDim[0]-1)*0.5
    #ymin = -1.0*(self.imDim[1]-1)*0.5
    xmin = -1.0*(self.imDim[1]-1)*0.5
    ymin = -1.0*(self.imDim[0]-1)*0.5

    #self.radon = np.zeros([self.nRho, self.nTheta])
    sTheta = np.sin(self.theta*DEGRAD)
    cTheta = np.cos(self.theta*DEGRAD)
    thetatest = np.abs(sTheta) >= (np.sqrt(2.) * 0.5)

    m = np.arange(self.imDim[1], dtype = np.uint32) # x values
    n = np.arange(self.imDim[0], dtype = np.uint32) # y values

    a = -1.0*np.where(thetatest == 1, cTheta, sTheta)
    a /= np.where(thetatest == 1, sTheta, cTheta)
    b = xmin*cTheta + ymin*sTheta

    outofbounds = self.imDim[0]*self.imDim[1]+1
    self.indexPlan = np.zeros([self.nRho,self.nTheta,self.imDim.max()],dtype=np.uint64)+outofbounds

    for i in np.arange(self.nTheta):
      b1 = self.rho - b[i]
      if thetatest[i]:
        b1 /= sTheta[i]
        b1 = b1.reshape(self.nRho, 1)
        indx_y = np.floor(a[i]*m+b1).astype(np.int64)
        indx_y = np.where(indx_y < 0, outofbounds, indx_y)
        indx_y = np.where(indx_y >= self.imDim[0], outofbounds, indx_y)
        #indx_y = np.clip(indx_y, 0, self.imDim[1])
        indx1D = np.clip(m+self.imDim[1]*indx_y, 0, outofbounds)
        self.indexPlan[:,i, 0:self.imDim[1]] = indx1D
      else:
        b1 /= cTheta[i]
        b1 = b1.reshape(self.nRho, 1)
        if cTheta[i] > 0:
          indx_x = np.floor(a[i]*n + b1).astype(np.int64)
        else:
          indx_x = np.ceil(a[i] * n + b1).astype(np.int64)
        indx_x = np.where(indx_x < 0, outofbounds, indx_x)
        indx_x = np.where(indx_x >= self.imDim[1], outofbounds, indx_x)
        indx1D = np.clip(indx_x+self.imDim[1]*n, 0, outofbounds)
        self.indexPlan[:, i, 0:self.imDim[0]] = indx1D
      self.indexPlan.sort(axis = -1)


  def radon_fast(self, imageIn, padding = np.array([0,0]), fixArtifacts = False, background = None):
    tic = timer()
    shapeIm = np.shape(imageIn)
    if imageIn.ndim == 2:
      nIm = 1
      image = imageIn[np.newaxis, : ,:]
      reform = True
    else:
      nIm = shapeIm[0]
      reform = False

    if background is None:
      image = imageIn.reshape(-1)
    else:
      image = imageIn - background
      image = image.reshape(-1)

    nPx = shapeIm[-1]*shapeIm[-2]
    im = np.zeros(nPx+1, dtype=np.float32)
    #radon = np.zeros([nIm, self.nRho, self.nTheta], dtype=np.float32)
    radon = np.zeros([nIm,self.nRho + 2 * padding[0],self.nTheta + 2 * padding[1]],dtype=np.float32)
    shpRdn = radon.shape
    norm = np.sum(self.indexPlan < nPx, axis = 2 ) + 1.0e-12
    for i in np.arange(nIm):
      im[:-1] = image[i,:,:].flatten()
      radon[i, padding[0]:shpRdn[1]-padding[0], padding[1]:shpRdn[2]-padding[1]] = np.sum(im.take(self.indexPlan.astype(np.int64)), axis=2) / norm

    if (fixArtifacts == True):
      radon[:,:,0] = radon[:,:,1]
      radon[:,:,-1] = radon[:,:,-2]

    radon = np.transpose(radon, [1,2,0]).copy()

    if reform==True:
      image = image.reshape(shapeIm)

    #print(timer()-tic)
    return radon

  def radon_faster(self,imageIn,padding = np.array([0,0]), fixArtifacts = False, background = None):
    tic = timer()
    shapeIm = np.shape(imageIn)
    if imageIn.ndim == 2:
      nIm = 1
      #image = image[np.newaxis, : ,:]
      #reform = True
    else:
      nIm = shapeIm[0]
    #  reform = False

    if background is None:
      image = imageIn.reshape(-1)
    else:
      image = imageIn - background
      image = image.reshape(-1)

    nPx = shapeIm[-1]*shapeIm[-2]
    indxDim = np.asarray(self.indexPlan.shape)
    #radon = np.zeros([nIm, self.nRho+2*padding[0], self.nTheta+2*padding[1]], dtype=np.float32)
    radon = np.zeros([self.nRho + 2 * padding[0],self.nTheta + 2 * padding[1], nIm],dtype=np.float32)
    shp = radon.shape

    counter = self.rdn_loops(image,self.indexPlan,nIm,nPx,indxDim,radon, np.asarray(padding))

    if (fixArtifacts == True):
      radon[:,padding[1],:] = radon[:,padding[1]+1,:]
      radon[:,shp[1]-1-padding[1],:] = radon[:,shp[1]-padding[1]-2,:]


    image = image.reshape(shapeIm)

    #print(timer()-tic)
    return radon#, counter

  @staticmethod
  @jit(nopython=True, fastmath=True, cache=True, parallel=False)
  def rdn_loops(images,index,nIm,nPx,indxdim,radon, padding):
    nRho = indxdim[0]
    nTheta = indxdim[1]
    nIndex = indxdim[2]
    #counter = np.zeros((nRho, nTheta, nIm), dtype=np.float32)
    count = 0.0
    sum = 0.0
    for q in prange(nIm):
      #radon[:,:,q] = np.mean(images[q*nPx:(q+1)*nPx])
      imstart = q*nPx
      for i in range(nRho):
        ip = i+padding[0]
        for j in range(nTheta):
          jp = j+padding[1]
          count = 0.0
          sum = 0.0
          for k in range(nIndex):
            indx1 = index[i,j,k]
            if (indx1 >= nPx):
              break
            #radon[q, i, j] += images[imstart+indx1]
            sum += images[imstart + indx1]
            count += 1.0
          #if count >= 1.0:
            #counter[ip,jp, q] = count
          radon[ip,jp,q] = sum/(count + 1.0e-12)
    #return counter

  #