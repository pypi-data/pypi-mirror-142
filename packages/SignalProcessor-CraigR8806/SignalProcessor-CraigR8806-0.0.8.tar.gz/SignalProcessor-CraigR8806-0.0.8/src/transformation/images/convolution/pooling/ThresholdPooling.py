from transformation.images.convolution.pooling.Pooling import Pooling
import numpy as np


class ThresholdPooling(Pooling):

    def __init__(self, size, threshold):
        super().__init__(size)
        self.threshold = threshold

    def pool(self, matrix):
        return 255 if np.average(matrix) >= self.threshold else 0

    def transform(self, image):
        return super().transform(image)