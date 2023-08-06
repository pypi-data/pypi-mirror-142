from abc import ABC, abstractmethod
from transformation.images.convolution.Convolution import Convolution
from transformation.images.filter.Filter import Filter

class Suppression(Convolution, ABC):

    def __init__(self, filterSize):
        super().__init__([Filter(filterSize)])
        
    def transform(self, image):
        return self.convolve(image)

    @abstractmethod
    def suppress(self):
        pass

    def _convoleOperation(self, row, column, channels, image):
        outpixel=[]
        for channel in range(channels):
            outpixel.append(self.supress(image[row:row+self.filterSize, column:column+self.filterSize, channel]))
        return outpixel
    