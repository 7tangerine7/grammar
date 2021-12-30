import cv2 as cv
import numpy as np
import os


def f(sample, state, d, row_s, row_e, col_s, col_e):
    if state == 0:
        return q(sample, standard_zero)
    elif state == 1:
        return q(sample, standard_one)
    else:
        h_check = False
        for iii in range(row_s+1, row_e):
            for kU in range(state+1):
                for kD in range(state + 1):
                    if (kU, kD) in vertical:
                        h_check = h_check or (d[kD, row_s, iii, col_s, col_e] and d[kU, iii+1, row_e, col_s, col_e]
                                              and vertical[(kU, kD)] == state)
        w_check = False
        for jjj in range(col_s+1, col_e):
            for kL in range(state+1):
                for kR in range(state+1):
                    if (kL, kR) in horizontal:
                        w_check = w_check or (d[kL, row_s, row_e, col_s, jjj] and d[kR, row_s, row_e, jjj+1, col_e] and
                                              horizontal[(kL, kR)] == state)
        r_check = False
        for kkk in range(2):
            if kkk in rename:
                r_check = r_check or (d[kkk, row_s, row_e, col_s, col_e] and rename[kkk])
    return h_check or w_check or r_check


def q(sample, standard):
    if np.shape(sample) == np.shape(standard):
        if np.equal(sample, standard):
            return True
    else:
        return False


def CYK(test):
    H, W = np.shape(test)
    num_col = W // w
    d = np.empty((12, 3, 3, num_col, num_col))
    it_v_s, it_v_e, it_g_s, it_g_e = 0, 0, 0, 0
    for s in range(h*w, H*W+1, h*w):
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
                                sample_ = test[i:i_end+1][j:j_end+1]
                                d[k, row_s_, row_e_, col_s_, col_e_] = f(sample_, k, d, row_s_, row_e_, col_s_, col_e_)
    if np.any(d[:, 0, 2, 0, num_col-1]) == 1:
        return True
    else:
        return False


def main():
    v1 = np.concatenate((standard_zero, standard_zero, standard_one), axis=0)
    v2 = np.concatenate((standard_zero, standard_zero, standard_one), axis=0)
    v3 = np.concatenate((standard_zero, standard_one, standard_zero), axis=0)
    test = np.concatenate((v1, v2, v3), axis=1)
    answer = CYK(test)
    if answer is True:
        print("Correct!")
    else:
        print("Incorrect")


if __name__ == '__main__':
    script_dir_1 = os.path.dirname('1.png')
    print(script_dir_1)
    script_dir_0 = os.path.dirname('0.png')
    file_path_1 = os.path.join(script_dir_1, '1.png')
    file_path_0 = os.path.join(script_dir_1, '0.png')
    standard_one = cv.imread(file_path_1, cv.IMREAD_GRAYSCALE)
    standard_zero = cv.imread(file_path_0, cv.IMREAD_GRAYSCALE)
    print(standard_one)
    h, w = np.shape(standard_zero)
    horizontal = {
        (10, 6): 10,
        (11, 9): 11,
        (10, 7): 11,
        (11, 8): 11
    }
    rename = {
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