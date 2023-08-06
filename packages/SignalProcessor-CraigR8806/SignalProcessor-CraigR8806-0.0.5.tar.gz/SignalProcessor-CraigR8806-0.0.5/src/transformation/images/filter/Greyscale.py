from transformation.images.ImageTransformation import ImageTransformation
import numpy as np

class Greyscale(ImageTransformation):

    def __init__(self):
        super().__init__()

    def transform(self, image):
        height=image.shape[0]
        width=image.shape[1]
        channels=image.shape[2]

        image = image.ravel()
        image = np.array([[int(np.sum(image[i:i+channels])/channels)] for i in range(0, len(image), channels)])
        image.shape = (height, width, 1)
        return image