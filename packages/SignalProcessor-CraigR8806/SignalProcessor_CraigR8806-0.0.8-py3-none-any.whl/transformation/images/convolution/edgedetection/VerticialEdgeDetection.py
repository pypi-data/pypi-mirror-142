from transformation.images.convolution.edgedetection.EdgeDetection import EdgeDetection
from transformation.images.convolution.Kernel import Kernel
from parallellinear.datatypes.Matrix import Matrix

class VerticalEdgeDetection(EdgeDetection):


    def __init__(self, kernelSize):
        template=[0 for i in range(kernelSize)]
        template[0] = 1
        template[-1] = -1
        matrix=[]
        for i in range(kernelSize):
            matrix.extend(template)
        kernel = Kernel(kernelSize, Matrix.fromFlatListGivenRowNumber(kernelSize, matrix))
        super().__init__(kernel)

    def transform(self, image):
        return super().transform(image)

    


