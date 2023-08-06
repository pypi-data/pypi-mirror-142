from abc import ABC, abstractmethod
from transformation.images.convolution.Convolution import Convolution
from transformation.images.filter.Filter import Filter
import numpy as np


class Pooling(Convolution, ABC):

    def __init__(self, filterLength):
        super().__init__([Filter(filterLength)])
        

    @abstractmethod
    def pool(self, matrix):
        pass

    def transform(self, image):
        return super().convolve(image)

    def _convoleOperation(self, row, column, channels, image):
        outpixel=[]
        for channel in range(channels):
            outpixel.append(self.pool(image[row:row+self.filterSize, column:column+self.filterSize, channel]))
        return outpixel




