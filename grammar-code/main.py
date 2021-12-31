import cv2 as cv
import numpy as np
import os


def f(sample, state, d, row_s, row_e, col_s, col_e):
    if state == 0:
        return q(sample, standard_zero)
    elif state == 1:
        return q(sample, standard_one)
    elif not np.any(d[state, row_s, row_e, col_s, col_e]):
        h_check = False
        for iii in range(row_s, row_e):
            for kU in range(state):
                for kD in range(state):
                    if (kU, kD) in vertical:
                        h_check = h_check or (d[kU, row_s, iii, col_s, col_e] and d[kD, iii+1, row_e, col_s, col_e]
                                              and vertical[(kU, kD)] == state)
        w_check = False
        for jjj in range(col_s, col_e):
            for kL in range(12):
                for kR in range(12):
                    if (kL, kR) in horizontal:
                        w_check = w_check or (d[kL, row_s, row_e, col_s, jjj] and d[kR, row_s, row_e, jjj+1, col_e] and
                                              horizontal[(kL, kR)] == state)
        r_check = False
        for kkk in range(6, 12):
            if kkk in rename:
                r_check = r_check or (d[kkk, row_s, row_e, col_s, col_e] and rename[kkk] == state)
        return h_check or w_check or r_check
    return False


def q(sample, standard):
    """
    >>> q(np.array([[1, 1], [1, 1]]), np.array([[1, 1], [1, 1]]))
    True
    """
    return np.array_equal(sample, standard)


def CYK(test):
    H, W = np.shape(test)
    num_col = W // w
    d = np.zeros((12, 3, 3, num_col, num_col), dtype=bool)
    for s in range(h*w, H*W+1, h*w):
        for i in range(0, H, h):
            if s > 1419 and i == 2*h: continue
            for j in range(W-w, -w+1, -w):
                for i_end in range(i+h, H+1, h):
                    for j_end in range(W, j, -w):
                        if (i_end - i)*(j_end - j) != s:
                            continue
                        else:
                            sample_ = test[i:i_end, j:j_end]
                            for k in range(12):
                                if i != 0:
                                    row_s_ = i//h
                                else:
                                    row_s_ = 0
                                row_e_ = i_end//h - 1
                                if j != 0:
                                    col_s_ = j//w
                                else:
                                    col_s_ = 0
                                col_e_ = j_end//w - 1
                                d[k, row_s_, row_e_, col_s_, col_e_] = f(sample_, k, d, row_s_, row_e_, col_s_, col_e_)
    if np.any(d[:, 0, 2, 0, num_col-1] == 1) and not d[6, 0, 2, num_col-1, num_col-1]  \
            and not d[8, 0, 2, num_col-1, num_col-1]:
        print("Correct!")
        if d[9, 0, 2, 0, 0] or d[8, 0, 2, 0, 0]:
            print("Без переносу")
        if d[7, 0, 2, 0, 0] or d[6, 0, 2, 0, 0]:
            print("З переносом")
    else:
        print("Incorrect")


def main():
    """
    v1 = np.concatenate((standard_one, standard_zero, standard_one), axis=1)
    v2 = np.concatenate((standard_zero, standard_one, standard_one), axis=1)
    v3 = np.concatenate((standard_one, standard_zero, standard_zero), axis=1)
    test = np.concatenate((v1, v2, v3), axis=0)
    """
    CYK(test)


if __name__ == '__main__':

    script_dir_1 = os.path.dirname('one.png')
    script_dir_0 = os.path.dirname('zero.png')
    script_dir_t = os.path.dirname('bad-example.png')
    file_path_1 = os.path.join(script_dir_1, 'one.png')
    file_path_0 = os.path.join(script_dir_1, 'zero.png')
    file_path_t = os.path.join(script_dir_t, 'bad-example.png')
    standard_one = cv.imread(file_path_1, cv.IMREAD_GRAYSCALE)
    standard_zero = cv.imread(file_path_0, cv.IMREAD_GRAYSCALE)
    test = cv.imread(file_path_t, cv.IMREAD_GRAYSCALE)
    h, w = np.shape(standard_zero)
    horizontal = {
        (6, 10): 10,
        (7, 11): 10,
        (8, 10): 11,
        (9, 11): 11
    }
    rename = {
        7: 10,
        9: 11
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
