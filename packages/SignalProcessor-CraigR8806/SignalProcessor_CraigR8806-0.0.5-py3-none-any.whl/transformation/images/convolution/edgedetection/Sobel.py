from abc import ABC
from transformation.images.convolution.edgedetection.EdgeDetection import EdgeDetection


class Sobel(EdgeDetection, ABC):

    def __init__(self, kernel):
        super().__init__(kernel)


    def transform(self, image):
        return super().transform(image)