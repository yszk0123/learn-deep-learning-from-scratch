import numpy as np
from examples.common.util import im2col


class ConvolutionLayer:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = int(1 + (H + 2 * self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2 * self.pad - FW) / self.stride)

        col_x = im2col(x, FH, FW, stride=self.stride, pad=self.pad)
        col_W = self.W.reshape(FN, -1).T
        out = np.dot(col_x, col_W) + self.b

        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out

    def backward(self, dout):
        raise Exception("To Be Implemented")
