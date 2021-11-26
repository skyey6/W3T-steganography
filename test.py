import cv2 as cv
import lsb
import henon
import arnold
import encrypt
import utils


def hide_something(cover, secret, key):
    secret_encrypted = encrypt.img_encrypt(secret, key)
    for i in range(7):  # 7次Arnold置乱
        secret_encrypted = arnold.arnold(secret_encrypted)
    secret_encrypted_arnold = secret_encrypted
    hided = lsb.LSB(cover, secret_encrypted_arnold)
    return hided


def extract_secret(target, shape, key):
    secret_encrypted_arnold = lsb.de_LSB(target, shape)
    for i in range(7):
        secret_encrypted_arnold = arnold.de_arnold(secret_encrypted_arnold)
    secret_encrypted = secret_encrypted_arnold
    secret = encrypt.img_decrypt(secret_encrypted, key)
    return secret


def hide_something_v2(cover, secret, key):
    """
    :param cover: 用于隐藏秘密信息的图片，一张RGB图
    :param secret: 秘密信息图片
    :param key: 密钥，int型，0~4,294,967,295
    :return: 隐藏了秘密信息的图片，一张RGB图
    """
    secret_encrypted = encrypt.img_encrypt(secret, key)
    # henon置乱
    cv.imwrite('img/henon.png', secret_encrypted)
    henon.HenonEncryption('img/henon.png', (0.1, 0.1))
    secret_encrypted_henon = cv.imread('img/henon_HenonEnc.png')
    for i in range(7):  # 7次Arnold置乱
        secret_encrypted_henon = arnold.arnold(secret_encrypted_henon)
    secret_encrypted_hybrid = secret_encrypted_henon
    hided = lsb.LSB(cover, secret_encrypted_hybrid)
    return hided


def extract_secret_v2(target, shape, key):
    """
    :param target: 隐藏了秘密信息的图片，一张RGB图
    :param shape: 秘密信息图片的shape:(h, w)
    :param key: 密钥，int型，0~4,294,967,295
    :return: 秘密信息图片
    """
    secret_encrypted_hybrid = lsb.de_LSB(target, shape)
    for i in range(7):
        secret_encrypted_hybrid = arnold.de_arnold(secret_encrypted_hybrid)
    secret_encrypted_henon = secret_encrypted_hybrid
    cv.imwrite('img/henon_HenonEnc.png', secret_encrypted_henon)
    henon.HenonDecryption('img/henon_HenonEnc.png', (0.1, 0.1))
    secret_encrypted = cv.imread('img/henon_HenonDec.png')
    secret = encrypt.img_decrypt(secret_encrypted, key)
    return secret


if __name__ == '__main__':
    # # 用于隐藏秘密信息的载体
    # cover = cv.imread('img/never777.png')
    # # 秘密信息
    # img = cv.imread('img/QRcode.png')
    #
    # # 秘密信息隐藏
    # a_img = hide_something_v2(cover, img, 777777777)
    # cv.imwrite('img/never777_hide_test.png', a_img)

    # 秘密信息提取
    a_img = cv.imread('img/never777_hide_test.png')
    shape = (300, 300)
    b_img = extract_secret_v2(a_img, shape, 777777777)
    cv.imshow('b_img', b_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
