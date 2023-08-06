from transformation.images.convolution.supression.Suppression import Suppression


class NonMaximumSuppression(Suppression):

    def __init__(self, filterSize):
        super().__init__(filterSize)


    def transform(self, image):
        return super().transform(image)