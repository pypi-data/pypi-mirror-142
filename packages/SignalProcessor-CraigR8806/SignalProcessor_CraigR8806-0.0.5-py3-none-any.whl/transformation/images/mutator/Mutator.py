from abc import ABC, abstractmethod
from transformation.images.ImageTransformation import ImageTransformation
import numpy as np



class Mutator(ImageTransformation, ABC):

    def __init__(self, filterSize, sampleSize):
        super().__init__()
        self.filterSize=filterSize
        self.sampleSize=sampleSize
    
    def mutate(self, image):
        scalingFactor = self.filterSize / self.sampleSize
        outimage=np.zeros((int(np.ceil(image.shape[0]*scalingFactor)), int(np.ceil(image.shape[1]*scalingFactor)), image.shape[2]))
        height = image.shape[0]
        width = image.shape[1]
        channels = image.shape[2] if len(image.shape) > 2 else 1
        for row in range(0, height, self.sampleSize):
            if row+self.sampleSize > height:
                continue
            # print("Starting row: "+ str(row))
            for column in range(0, width, self.sampleSize):
                if column+self.sampleSize > width:
                    continue
                self._mutationOperation(row, column, channels, image, outimage)
        return outimage.astype(np.uint8)

    @abstractmethod
    def _mutationOperation(self, row, column, channels, image, outimage):
        pass