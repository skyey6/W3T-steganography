"""
图片加密
"""
import random
import cv2 as cv
import numpy as np


def img_encrypt(img, key):
    """
    :param img: 一张RGB图
    :param key: 密钥，int型，作为生成伪随机数的seed
    :return: 加密后的黑白图
    """
    random.seed(key)
    key_list = []
    key_bin_list = []
    for i in range(8):
        key_list.append(random.randint(1, 15))
    for i in key_list:
        for j in range(4):
            key_bin_list.append(str(bin(i)[2:].zfill(4))[j])

    if img.ndim == 3:  # 转灰度图
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 灰度图转黑白图
    thresh = 127
    img = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
    # 利用密钥 key_bin，对图像进行加密
    n = 0
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if h % 3 == 1 or h % 3 == 2:
                if key_bin_list[n] == '1':
                    if img[h, w] == 0:
                        img[h, w] = 255
                    else:
                        img[h, w] = 0
                n += 1
                if n == len(key_bin_list)-1:  # 最后1位弃用
                    n = 0
    for w in range(img.shape[1]):
        for h in range(img.shape[0]):
            if w % 3 == 1 or w % 3 == 2:
                if key_bin_list[n] == '1':
                    if img[h, w] == 0:
                        img[h, w] = 255
                    else:
                        img[h, w] = 0
                n += 1
                if n == len(key_bin_list)-1:  # 最后1位弃用
                    n = 0
    return img


def img_decrypt(img, key):
    """
    :param img: 一张RGB图
    :param key: 密钥，int型，作为生成伪随机数的seed
    :return: 解密后的黑白图
    """
    random.seed(key)
    key_list = []
    key_bin_list = []
    for i in range(8):
        key_list.append(random.randint(1, 15))
    for i in key_list:
        for j in range(4):
            key_bin_list.append(str(bin(i)[2:].zfill(4))[j])

    if img.ndim == 3:  # 转灰度图
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 灰度图转黑白图
    thresh = 127
    img = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
    # 利用密钥 key_bin，对图像进行解密
    n = 0
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if h % 3 == 1 or h % 3 == 2:
                if key_bin_list[n] == '1':
                    if img[h, w] == 0:
                        img[h, w] = 255
                    else:
                        img[h, w] = 0
                n += 1
                if n == len(key_bin_list) - 1:  # 最后1位弃用
                    n = 0
    for w in range(img.shape[1]):
        for h in range(img.shape[0]):
            if w % 3 == 1 or w % 3 == 2:
                if key_bin_list[n] == '1':
                    if img[h, w] == 0:
                        img[h, w] = 255
                    else:
                        img[h, w] = 0
                n += 1
                if n == len(key_bin_list) - 1:  # 最后1位弃用
                    n = 0
    return img


if __name__ == '__main__':
    path = 'img/QRcode.png'
    secret = cv.imread(path)

    secret_encrypted = img_encrypt(secret, 777777777)
    cv.imshow('secret_encrypted', secret_encrypted)
    secret_decrypted = img_decrypt(secret_encrypted, 777777777)
    cv.imshow('secret_decrypted', secret_decrypted)

    cv.waitKey(0)
    cv.destroyAllWindows()
