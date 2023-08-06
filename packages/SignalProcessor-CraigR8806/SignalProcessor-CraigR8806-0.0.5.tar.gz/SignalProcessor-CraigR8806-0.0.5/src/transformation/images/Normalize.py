from transformation.images.ImageTransformation import ImageTransformation
import numpy as np


class Normalize(ImageTransformation):

    def __init__(self, minValue, maxValue):
        super().__init__()
        self.minValue = minValue
        self.maxValue = maxValue
        

    def transform(self, image):
        max=np.max(image)
        min=np.min(image)
        return (((image - min)/(max - min))*((self.maxValue-self.minValue) + self.minValue)).astype(np.int32)