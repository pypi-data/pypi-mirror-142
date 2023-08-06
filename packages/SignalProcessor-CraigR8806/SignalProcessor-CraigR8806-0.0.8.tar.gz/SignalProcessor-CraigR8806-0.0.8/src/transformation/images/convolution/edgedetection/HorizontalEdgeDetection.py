from transformation.images.convolution.edgedetection.EdgeDetection import EdgeDetection
from transformation.images.convolution.Kernel import Kernel
from parallellinear.datatypes.Matrix import Matrix


class HorizontalEdgeDetection(EdgeDetection):
        

    def __init__(self, kernelSize):
        matrix=[1 for i in range(kernelSize)]
        [matrix.extend([0 for i in range(kernelSize)]) for i in range(kernelSize-2)]
        matrix.extend([-1 for i in range(kernelSize)])
        kernel = Kernel(kernelSize, Matrix.fromFlatListGivenRowNumber(kernelSize, matrix))
        super().__init__(kernel)

    def transform(self, image):
        return super().transform(image)