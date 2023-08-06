from transformation.images.mutator.Mutator import Mutator
import numpy as np


class Pixelator(Mutator):

    def __init__(self, filterSize):
        super().__init__(filterSize, filterSize)

    def transform(self, image):
        return super().mutate(image)

    def _mutationOperation(self, row, column, channels, image, outimage):
        subset = image[row:row+self.filterSize, column:column+self.filterSize]
        for channel in range(channels):
            outimage[row:row + self.filterSize, column:column + self.filterSize, channel] = np.average(subset[:,:,channel])