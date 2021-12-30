import cv2 as cv
import numpy as np


def f(sample, state, d, row_s, row_e, col_s, col_e):
    if state == 0:
        return q(sample, standard_zero)
    elif state == 1:
        return q(sample, standard_one)
    else:
        for iii in range(row_s, row_s+1):
            h =

def q(sample, standard):
    if sample == standard:
        return True
    else:
        return False


def CYK(test):
    H, W = np.shape(test)
    num_col = W / w
    d = np.empty((12, 3, 3, num_col, num_col))
    it_v_s, it_v_e, it_g_s, it_g_e = 0, 0, 0, 0
    for s in range(h*w, H*W, h*w):
        for i in range(0, H, h):
            it_v_s += 1
            for j in range(0, W, w):
                it_v_e += 1
                for i_end in range(i + h, H + h, h):
                    it_g_s += 1
                    for j_end in range(j + w, W + w, w):
                        it_g_e += 1
                        if (i_end - i)*(j_end - j) != s:
                            continue
                        else:
                            for k in range(12):
                                row_s = H//i
                                row_e = H//i_end
                                col_s = W//j
                                col_e = W//j_end
                                sample = test[i:i_end+1][j:j_end+1]
                                d[k, row_s, row_e, col_s, col_e] = f(sample, k, d, row_s, row_e, col_s, col_e)
    if np.any(d[:, 0, 2, 0, num_col-1]) == 1:
        return True
    else:
        return False


def main():
    v1 = np.concatenate((standard_zero, standard_zero, standard_zero), axis=0)
    v2 = np.concatenate((standard_zero, standard_zero, standard_zero), axis=0)
    v3 = np.concatenate((standard_zero, standard_zero, standard_zero), axis=0)
    test = np.concatenate((v1, v2, v3), axis=1)



if __name__ == '__main__':
    standard_one = cv.imread('1.ppm')
    standard_zero = cv.imread('0.ppm')
    h, w = np.shape(standard_zero)
    horizontal2 = {
        (10, 6): 10,
        (11, 9): 11,
        (10, 7): 11,
        (11, 8): 11
    }
    horizontal1 = {
        11: 9,
        10: 8
    }
    vertical = {
        (1, 1): 2,
        (1, 0): 3,
        (0, 1): 4,
        (0, 0): 5,
        (2, 1): 6,
        (3, 0): 6,
        (4, 0): 6,
        (2, 0): 7,
        (5, 1): 8,
        (5, 0): 9,
        (4, 1): 9,
        (3, 1): 9
    }
    main()