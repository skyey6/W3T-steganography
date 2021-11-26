"""
图片加密
"""
import cv2 as cv
import numpy as np


def img_encrypt(img, key):
    """
    :param img: 一张RGB图
    :param key: 密钥，int型，0~4,294,967,295
    :return: 加密后的黑白图
    """
    if key > 4294967295:
        raise ValueError("密钥过大！")
    key_bin_list = [int(x) for x in bin(key)[2:].zfill(32)]  # 转成32位二进制数，每个数字存入列表中
    if img.ndim == 3:  # 转灰度图
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 灰度图转黑白图
    thresh = 127
    img = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
    # 利用密钥 key_bin，对图像进行加密
    n = 0
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if key_bin_list[n] == 1:
                if img[h, w] == 0:
                    img[h, w] = 255
                else:
                    img[h, w] = 0
            n += 1
            if n == 32:
                n = 0
    return img


def img_decrypt(img, key):
    """
    :param img: 一张RGB图
    :param key: 密钥，int型，0~4,294,967,295
    :return: 解密后的黑白图
    """
    if key > 4294967295:
        raise ValueError("密钥过大！")
    key_bin_list = [int(x) for x in bin(key)[2:].zfill(32)]  # 转成32位二进制数，每个数字存入列表中
    if img.ndim == 3:  # 转灰度图
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 灰度图转黑白图
    thresh = 127
    img = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
    # 利用密钥 key_bin，对图像进行解密
    n = 0
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if key_bin_list[n] == 1:
                if img[h, w] == 0:
                    img[h, w] = 255
                else:
                    img[h, w] = 0
            n += 1
            if n == 32:
                n = 0
    return img


if __name__ == '__main__':
    path = 'img/lena.jpg'
    secret = cv.imread(path)
    # encrypted = img_encrypt(secret, 777777)
    # cv.imwrite('img/secret_encrypted.jpg', encrypted)
    # secret_encrypted = cv.imread('img/secret_encrypted.jpg')
    # cv.imshow('secret_encrypted', secret_encrypted)
    # secret_decrypted = img_decrypt(secret_encrypted, 777777)
    # cv.imshow('secret_decrypted', secret_decrypted)

    secret_encrypted = img_encrypt(secret, 777777777)
    cv.imshow('secret_encrypted', secret_encrypted)
    secret_decrypted = img_decrypt(secret_encrypted, 777777777)
    cv.imshow('secret_decrypted', secret_decrypted)

    cv.waitKey(0)
    cv.destroyAllWindows()
