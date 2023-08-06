from transformation.images.convolution.edgedetection.Sobel import Sobel
from transformation.images.convolution.Kernel import Kernel
from parallellinear.datatypes.Matrix import Matrix
import numpy as np



class HorizontalSobel(Sobel):

    def __init__(self, kernelSize):

        center = kernelSize // 2

        matrix = np.mgrid[0 - center : kernelSize - center, 0 - center : kernelSize - center][0]
        matrix[:, center] = matrix[:, center] * 2
        matrix = list(np.flip(matrix).flat)

        kernel = Kernel(kernelSize, Matrix.fromFlatListGivenRowNumber(kernelSize, matrix))
        super().__init__(kernel)

    def transform(self, image):
        return super().transform(image)
