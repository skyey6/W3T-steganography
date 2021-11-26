import cv2
import numpy as np


def LSB(target, secret):
    """
    :param target: 携带秘密信息的载体，一张RGB图，.png格式
    :param secret: 秘密信息，一张RGB图
    :return: 隐藏了秘密信息的载体
    """
    if secret.ndim == 3:    # 转灰度图
        secret = cv2.cvtColor(secret, cv2.COLOR_BGR2GRAY)
    # 灰度图转黑白图
    thresh = 127
    secret = cv2.threshold(secret, thresh, 255, cv2.THRESH_BINARY)[1]
    h, w = secret.shape
    # print(secret.shape)
    # print(target.shape)
    # 隐藏在蓝色通道中
    for i in range(h):
        for j in range(w):
            if (secret[i, j] > thresh) and (target[i, j, 0]%2 == 0):
                target[i, j, 0] += 1
            elif (secret[i, j] <= thresh) and (target[i, j, 0]%2 != 0):
                target[i, j, 0] -= 1
    return target


def de_LSB(target, shape):
    """
    :param target: 隐藏着秘密的载体，一张RGB图，.png格式
    :param shape: 秘密图片的shape:(h, w)
    :return: 秘密图片
    """
    secret_img = np.zeros(shape)
    # 从载体的蓝色通道中提取秘密信息
    for i in range(shape[0]):
        for j in range(shape[1]):
            if target[i, j, 0]%2 != 0:
                secret_img[i, j] = 255
    return secret_img


if __name__ == '__main__':

    # LSB隐写
    cover = cv2.imread('img/never800.jpg')
    secret = cv2.imread('img/secret.jpg')
    cv2.imshow('secret', secret)
    cover_hide = LSB(cover, secret)
    # cv2.imwrite('img/never800_hide2.png', cover_hide)
    cv2.imshow('cover_hide', cover_hide)
    never800_hide = cv2.imread('img/never800_hide2.png')
    ex = de_LSB(never800_hide, secret.shape)
    cv2.imshow('extract', ex)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

