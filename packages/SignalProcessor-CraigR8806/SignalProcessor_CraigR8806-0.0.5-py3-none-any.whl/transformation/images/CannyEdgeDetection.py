from transformation.images.ImageTransformation import ImageTransformation
from transformation.images.convolution.edgedetection.SobelProcessing import SobelProcessing
from transformation.images.convolution.distortion.blur.GaussianBlur import GaussianBlur
from transformation.images.convolution.pooling.ThresholdPooling import ThresholdPooling
from transformation.images.filter.Greyscale import Greyscale
from transformation.images.Normalize import Normalize



class CanneyEdgeDetection(ImageTransformation):

    def __init__(self, sobelProcessor, gaussianProcessor, thresholdPooling=None, gaussianPasses=1):
        super().__init__()
        self.sobelProcessor = sobelProcessor
        self.gaussianProcessor = gaussianProcessor
        self.thresholdPooling = thresholdPooling
        self.gaussianPasses = gaussianPasses
        

    @classmethod
    def withThreshold(cls, sobelSize, thresholdFilterSize, threshold, gaussianSize, gaussianSigma, gaussianPasses=1):
        sobelProcessor = SobelProcessing(sobelSize)
        gaussianProcessor = GaussianBlur(gaussianSize, gaussianSigma)
        thresholdPooling = ThresholdPooling(thresholdFilterSize, threshold)
        return cls(sobelProcessor=sobelProcessor, gaussianProcessor=gaussianProcessor, thresholdPooling=thresholdPooling, gaussianPasses=gaussianPasses)

    @classmethod
    def withoutThreshold(cls, sobelSize, gaussianSize, gaussianSigma, gaussianPasses=1):
        sobelProcessor = SobelProcessing(sobelSize)
        gaussianProcessor = GaussianBlur(gaussianSize, gaussianSigma)
        return cls(sobelProcessor=sobelProcessor, gaussianProcessor=gaussianProcessor, gaussianPasses=gaussianPasses)



    def transform(self, image):
        greyscaleFilter = Greyscale()

        if len(image.shape)>2:
            image = greyscaleFilter.transform(image)
        else:
            image.shape = (image.shape[0], image.shape[1], 1)
        for i in range(self.gaussianPasses):
            image = self.gaussianProcessor.transform(image)

        image = self.sobelProcessor.transform(image)

        if self.thresholdPooling != None:
            image = self.thresholdPooling.transform(image)

        return image









