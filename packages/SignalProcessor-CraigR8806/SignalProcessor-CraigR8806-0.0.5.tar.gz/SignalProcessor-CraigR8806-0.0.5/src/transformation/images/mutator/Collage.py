from transformation.images.mutator.Mutator import Mutator
import numpy as np
from PIL import Image
import glob

class Collage(Mutator):


    def __init__(self, filterSize, sampleSize):
        super().__init__(filterSize, sampleSize)
        self.compositionImages = []

    def transform(self, image):
        return super().mutate(image)

    def _mutationOperation(self, row, column, channels, image, outimage):
        sampleSubset = image[row:row+self.sampleSize, column:column+self.sampleSize]
        compositionPath = self._getClosestCompositionImagePath(sampleSubset)
        oirow = int(row/self.sampleSize)*self.filterSize
        oicol = int(column/self.sampleSize)*self.filterSize
        outimage[oirow:oirow+self.filterSize, oicol:oicol+self.filterSize] = self._getScaledImageDataGivenPath(compositionPath)

    def loadCompositionImages(self, basePath):
        for entry in glob.glob(basePath + "/**/*"):
            self._addImageToCompositionImagesByPath(entry)



    def _getAvgColorFromSample(self, sample):
        if len(sample.shape) < 3:
            sample.shape = (sample.shape[0], sample.shape[1], 1)
        return [int(np.average(sample[:,:,channel])) for channel in range(sample.shape[2])]

    def _getColorDistance(self, cA, cB):
        return np.sqrt(np.sum([np.square(cA[channel]-cB[channel]) for channel in range(len(cA))]))

    def _getClosestCompositionImagePath(self, sampleSubset):
        avgColorOfSample = self._getAvgColorFromSample(sampleSubset)
        indexToDistance={}
        index=0
        for image in self.compositionImages:
            indexToDistance[index] = self._getColorDistance(avgColorOfSample, image['avgColor'])
            index+=1
        s = sorted(indexToDistance.items(), key=lambda x:x[1])
        closest=[s[0][0]]
        if abs(s[0][1] - s[1][1]) < 0.15:
            closest = [entry[0] for entry in s if entry[1]-s[0][1] < 0.15]
        paths =  self.compositionImages[closest[np.random.randint(0, len(closest))]]['paths']
        return paths[np.random.randint(0, len(paths))]


    def _scaleImage(self, image):
        return image.resize((self.filterSize, self.filterSize), Image.ANTIALIAS)

    def _addImageToCompositionImagesByPath(self, path):
        imdata = self._getScaledImageDataGivenPath(path)
        avgColor = self._getAvgColorFromSample(imdata)
        index = self._getCompositionImagesIndexByColor(avgColor)
        if index == -1:
            self.compositionImages.append({"avgColor":avgColor, "paths":[path]})
        else:
            self.compositionImages[index]["paths"].append(path)

    def _getCompositionImagesIndexByColor(self, color):
        outIndex = -1
        index = 0
        for image in self.compositionImages:
            if image['avgColor'] == color:
                outIndex = index
                break
        return outIndex

    def _getImageDataFromPILImage(self, pilimage):
        imdata = np.array(pilimage.getdata())
        imdata.shape = (pilimage.width, pilimage.height, imdata.shape[1])
        return imdata

    def _getScaledImageDataGivenPath(self, path):
        im = Image.open(path)
        im = self._scaleImage(im)
        imdata = self._getImageDataFromPILImage(im)
        im.close()
        return imdata
        