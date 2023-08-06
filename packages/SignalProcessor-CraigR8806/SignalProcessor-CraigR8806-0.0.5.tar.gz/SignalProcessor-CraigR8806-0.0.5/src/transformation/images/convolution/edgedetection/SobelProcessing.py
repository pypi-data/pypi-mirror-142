from transformation.images.convolution.Convolution import Convolution
from transformation.images.convolution.edgedetection.VerticalSobel import VerticalSobel
from transformation.images.convolution.edgedetection.HorizontalSobel import HorizontalSobel
from transformation.images.Normalize import Normalize
from parallellinear.datatypes.Matrix import Matrix
import numpy as np


class SobelProcessing(Convolution):


    def __init__(self, kernelSize):
        super().__init__([HorizontalSobel(kernelSize).getKernel(), VerticalSobel(kernelSize).getKernel()])
        self.operations = {"sobel" : self._sobel, "nonmaximum" : self._nonmaximum, "threshold" : self._thresholding, "tracing" : self._tracing}

    def transform(self, image):
        self.sX = np.ndarray((image.shape))
        self.sY = np.ndarray((image.shape))
        self.step = "sobel"
        g = self.convolve(image)
        g = Normalize(0, 255).transform(g)
        self.phase = np.arctan2(self.sY, self.sX) * 180 / np.pi
        self.step = "nonmaximum"
        out = self.convolve(g)
        self.thresholdValues = np.zeros(image.shape)
        self.strongIndicies = []
        maxValue = np.max(out)
        self.low, self.high = 0.15 * maxValue, 1 * maxValue
        self.step = "threshold"
        self.convolve(out)

        print(out.shape)

        self.vis = np.zeros(out.shape, bool)
        self.dx = [1, 0, -1,  0, -1, -1, 1,  1]
        self.dy = [0, 1,  0, -1,  1, -1, 1, -1]
        for s in self.strongIndicies:
            if not self.vis[s]:
                self._dfs(s)


        self.step = "tracing"
        out = self.convolve(out)

        return out


    def _convoleOperation(self, row, column, channels, image):
        outpixel = []
        for channel in range(channels):
            outpixel.append(self.operations[self.step](row, column, channel, image))
        return outpixel


    def _sobel(self, row, column, channel, image):
        subset = list(image[row:row+self.filterSize, column:column+self.filterSize, channel].flat)
        self.sY[row, column, channel] = self.kernels[0].getMatrix().elementWiseMultiply(Matrix.fromFlatListGivenRowNumber(self.filterSize, subset), in_place=False).sum()
        self.sX[row, column, channel] = self.kernels[1].getMatrix().elementWiseMultiply(Matrix.fromFlatListGivenRowNumber(self.filterSize, subset), in_place=False).sum()
        return np.sqrt(np.square(self.sX[row, column]) + np.square(self.sY[row, column]))

    def _nonmaximum(self, row, column, channel, image):
        out = 0
        if self.phase[row, column, channel] < 0:
            self.phase[row, column, channel] += 360
        if ((column+1) < image.shape[1]) and ((column-1) >= 0) and ((row+1) < image.shape[0]) and ((row-1) >= 0):
            if (self.phase[row, column, channel] >= 337.5 or self.phase[row, column, channel] < 22.5) or (self.phase[row, column, channel] >= 157.5 and self.phase[row, column, channel] < 202.5):
                if image[row, column, channel] >= image[row, column + 1, channel] and image[row, column, channel] >= image[row, column - 1, channel]:
                    out = image[row, column, channel].tolist()[0]
            if (self.phase[row, column, channel] >= 22.5 and self.phase[row, column, channel] < 67.5) or (self.phase[row, column, channel] >= 202.5 and self.phase[row, column, channel] < 247.5):
                if image[row, column, channel] >= image[row - 1, column + 1, channel] and image[row, column, channel] >= image[row + 1, column - 1, channel]:
                    out = image[row, column, channel].tolist()[0]
            if (self.phase[row, column, channel] >= 67.5 and self.phase[row, column, channel] < 112.5) or (self.phase[row, column, channel] >= 247.5 and self.phase[row, column, channel] < 292.5):
                if image[row, column, channel] >= image[row - 1, column, channel] and image[row, column, channel] >= image[row + 1, column, channel]:
                    out = image[row, column, channel].tolist()[0]
            if (self.phase[row, column, channel] >= 112.5 and self.phase[row, column, channel] < 157.5) or (self.phase[row, column, channel] >= 292.5 and self.phase[row, column, channel] < 337.5):
                if image[row, column, channel] >= image[row - 1, column - 1, channel] and image[row, column, channel] >= image[row + 1, column + 1, channel]:
                    out = image[row, column, channel].tolist()[0]
        return out

    def _thresholding(self, row, column, channel, image):
        if image[row, column, channel] >= self.high:
            self.thresholdValues[row, column, channel] = 1.0
            self.strongIndicies.append((row, column, channel))
        elif image[row, column, channel] >= self.low:
            self.thresholdValues[row, column, channel] = 0.5
        return 0

    def _tracing(self, row, column, channel, image):
        return 255 if self.vis[row, column, channel] else 0.0

    def _dfs(self, origin):
            q = [origin]
            while len(q) > 0:
                s = q.pop()
                self.vis[s] = True
                self.thresholdValues[s] = 1
                for channel in range(self.thresholdValues.shape[2]):
                    for k in range(len(self.dx)):
                        for c in range(1, 16):
                            index = (s[0] + c * self.dx[k], s[1] + c * self.dy[k], channel)
                            if self._validCoords(index, self.thresholdValues) and (self.thresholdValues[index] >= 0.5) and (not self.vis[index]):
                                q.append(index)
            pass

    def _validCoords(self, index, image):
        return index[0] >= 0 and index[0] < image.shape[0] and index[1] >= 0 and index[1] < image.shape[1]