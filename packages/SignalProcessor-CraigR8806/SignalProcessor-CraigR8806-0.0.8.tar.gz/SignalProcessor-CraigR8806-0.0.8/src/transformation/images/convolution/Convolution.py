from abc import ABC, abstractmethod
from transformation.images.ImageTransformation import ImageTransformation
from parallellinear.datatypes.Matrix import Matrix
import numpy as np


class Convolution(ImageTransformation, ABC):
    
    def __init__(self, kernels):
        super().__init__()
        self.kernels = kernels
        self.filterSize=kernels[0].getSize()
    
    def getKernels(self):
        return self.kernels
    
    def convolve(self, image):
        outimage=[]
        height = image.shape[0]
        width = image.shape[1]
        channels = image.shape[2] if len(image.shape) > 2 else 1
        for row in range(height):
            if row+self.filterSize > height:
                    continue
            # print("on row: " + str(row))
            outrow=[]
            for column in range(width):
                if column+self.filterSize > width:
                    continue
                outrow.append(self._convoleOperation(row, column, channels, image))
            outimage.append(outrow)
        return np.array(outimage)


    def _convoleOperation(self, row, column, channels, image):
        outpixel = []
        for channel in range(channels):
            subset = list(image[row:row+self.filterSize, column:column+self.filterSize, channel].flat)
            for kernel in self.kernels:
                outpixel.append(self._adjustOutgoingValue(kernel.getMatrix().elementWiseMultiply(Matrix.fromFlatListGivenRowNumber(self.filterSize, subset), in_place=False).sum()))
        return outpixel

    def _adjustOutgoingValue(self, value):
        return value