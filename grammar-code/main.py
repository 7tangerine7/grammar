import cv2 as cv
import numpy as np


def q(sample, standard_one, standard_zero):
    if sample == standard_one or sample == standard_zero:
        return True
    else:
        return False

'''
def make_test(order, standard_one, standard_zero):
'''

def g_horizontal():


def g_vertical():


def CYK(test, h, w):
    H, W = np.shape(test)
    num_col = W / w
    d = np.empty((12, 3, 3, num_col, num_col))
    for s in range(h*w, H*W, h*w):
        for i in range(0, H, h):
            for j in range(0, W, w):
                for i_end in range(i + h, H + h, h):
                    for j_end in range(j + w, W + w, w):
                        if (i_end - i)*(j_end - j) != s:
                            continue
                        else:


def main():
    standard_one = cv.imread('1.ppm')
    standard_zero = cv.imread('0.ppm')
    l, w = np.shape(standard_zero)
    v1 = np.concatenate((standard_zero, standard_zero, standard_zero), axis=0)
    v2 = np.concatenate((standard_zero, standard_zero, standard_zero), axis=0)
    v3 = np.concatenate((standard_zero, standard_zero, standard_zero), axis=0)
    test = np.concatenate((v1, v2, v3), axis=1)
