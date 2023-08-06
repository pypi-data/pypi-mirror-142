from transformation.images.mutator.Mutator import Mutator
import numpy as np


class RandomReorganizer(Mutator):

    def __init__(self, filterSize):
        super().__init__(filterSize, filterSize)

    def transform(self, image):
        return super().mutate(image)

    def _mutationOperation(self, row, column, channels, image, outimage):
        subset = list(image[row:row+self.filterSize, column:column+self.filterSize].flat)
        
        subset = np.array(subset)
        subset.shape = (self.filterSize*self.filterSize, 3)
        np.random.shuffle(subset)
        subset.shape = (self.filterSize, self.filterSize, 3)
        outimage[row:row + self.filterSize, column:column + self.filterSize] = subset

        