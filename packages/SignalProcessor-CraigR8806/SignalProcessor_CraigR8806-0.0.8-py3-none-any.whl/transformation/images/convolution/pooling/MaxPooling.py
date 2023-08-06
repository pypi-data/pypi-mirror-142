from transformation.images.convolution.pooling.Pooling import Pooling
import numpy as np

class MaxPooling(Pooling):

    def __init__(self, filterLength):
        super().__init__(filterLength)

    def pool(self, matrix):
        return np.max(matrix)

    def transform(self, image):
        return super().transform(image)