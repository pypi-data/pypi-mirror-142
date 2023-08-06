from abc import ABC
from transformation.images.convolution.Convolution import Convolution
from transformation.images.convolution.Kernel import Kernel
from parallellinear.datatypes.Matrix import Matrix



class EdgeDetection(Convolution, ABC):

    def __init__(self, kernel):
        super().__init__([kernel])


    def transform(self, image):
        return self.convolve(image)


    def getKernel(self):
        return self.kernels[0]
