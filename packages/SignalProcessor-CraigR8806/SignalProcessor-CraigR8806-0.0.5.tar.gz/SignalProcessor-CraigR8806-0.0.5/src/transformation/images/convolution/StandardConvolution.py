from transformation.images.convolution.Convolution import Convolution
from transformation.images.convolution.Kernel import Kernel


class StandardConvolution(Convolution):


    def __init__(self, kernels):
        super().__init__(kernels)


    @classmethod
    def randomKernel(cls, kernelSize, calcManager=None, random_low=0, random_high=1):
        kernels=[Kernel.random(kernelSize, calcManager=calcManager, random_low=random_low, random_high=random_high)]
        return cls(kernels)


    def transform(self, image):
        return self.convolve(image)
