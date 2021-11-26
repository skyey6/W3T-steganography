"""
实现Arnold变换与复原变换
"""
import numpy as np
import cv2


def arnold(img):
    """
    Arnold置乱
    :param img: 要进行置乱的图片
    :return: 置乱后的img
    """
    if img.ndim == 3:    # 转灰度图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = 1
    b = 1
    h, w = img.shape
    N = h
    newImg = np.zeros((h, w), np.uint8)
    for x in range(h):
        for y in range(w):
            xx = (x + b * y) % N
            yy = ((a * x) + (a * b + 1) * y) % N
            newImg[yy, xx] = img[y, x]
    return newImg


def de_arnold(img):
    """
    Arnold置乱的复原变换
    :param img: 要进行复原的图片
    :return: 复原后的img
    """
    if img.ndim == 3:    # 转灰度图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = 1
    b = 1
    h, w = img.shape
    N = h
    newImg = np.zeros((h, w), np.uint8)
    for x in range(h):
        for y in range(w):
            xx = ((a * b + 1) * x - b * y) % N
            yy = (-a * x + y) % N
            newImg[yy, xx] = img[y, x]
    return newImg


if __name__ == '__main__':
    img = cv2.imread('img/lena.jpg', cv2.IMREAD_GRAYSCALE)  # 读取灰度图
    print(img.shape)

    cv2.imshow('lena', img)

    for i in range(7):
        img = arnold(img)
    cv2.imshow('lena2', img)

    for i in range(7):
        img = de_arnold(img)
    cv2.imshow('lena3', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()