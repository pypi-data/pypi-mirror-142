from transformation.images.mutator.Mutator import Mutator
import numpy as np

class ColorClassifier(Mutator):

    def __init__(self, filterSize, inverse=False):
        super().__init__(filterSize, filterSize)
        self.inverse = inverse
        self.colors = []


    def loadColors(self, colors:list):
        if type(colors[0]) == str:
            colors = [[(int(color, 16) >> 8*c)&255 for c in range(3)] for color in colors]
        
        self.colors = colors


    def transform(self, image):
        return super().mutate(image)

    def _mutationOperation(self, row, column, channels, image, outimage):
        sampleSubset = image[row:row+self.filterSize, column:column+self.filterSize]
        outimage[row:row+self.filterSize, column:column+self.filterSize] = self._getClosestColor(sampleSubset)


    def _getAvgColorFromSample(self, sample):
        if len(sample.shape) < 3:
            sample.shape = (sample.shape[0], sample.shape[1], 1)
        return [int(np.average(sample[:,:,channel])) for channel in range(sample.shape[2])]

    def _getColorDistance(self, cA, cB):
        return np.sqrt(np.sum([np.square(cA[channel]-cB[channel]) for channel in range(len(cA))]))

    def _getClosestColor(self, sampleSubset):
        avgColorOfSample = self._getAvgColorFromSample(sampleSubset)
        indexToDistance={}
        index=0
        for color in self.colors:
            indexToDistance[index] = self._getColorDistance(avgColorOfSample, color)
            index+=1
        return self.colors[sorted(indexToDistance.items(), key=lambda x:x[1])[-1 if self.inverse else 0][0]]