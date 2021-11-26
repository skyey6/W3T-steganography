"""
实现henon置乱与复原
"""
import cv2
import numpy as np
from matplotlib.pyplot import imshow
from PIL import Image


def dec(bitSequence):
    decimal = 0
    for bit in bitSequence:
        decimal = decimal * 2 + int(bit)
    return decimal


def getImageMatrix(imageName):
    im = Image.open(imageName)
    pix = im.load()
    color = 1
    if type(pix[0, 0]) == int:
        color = 0
    image_size = im.size
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
            row.append((pix[width, height]))
        image_matrix.append(row)
    return image_matrix, image_size[0], image_size[1], color


def genHenonMap(dimension, key):
    x = key[0]
    y = key[1]
    sequenceSize = dimension * dimension * 8  # Total Number of bitSequence produced
    bitSequence = []  # Each bitSequence contains 8 bits
    byteArray = []  # Each byteArray contains m( i.e 512 in this case) bitSequence
    TImageMatrix = []  # Each TImageMatrix contains m*n byteArray( i.e 512 byteArray in this case)
    for i in range(sequenceSize):
        xN = y + 1 - 1.4 * x ** 2
        yN = 0.3 * x

        x = xN
        y = yN

        if xN <= 0.4:
            bit = 0
        else:
            bit = 1

        try:
            bitSequence.append(bit)
        except:
            bitSequence = [bit]

        if i % 8 == 7:
            decimal = dec(bitSequence)
            try:
                byteArray.append(decimal)
            except:
                byteArray = [decimal]
            bitSequence = []

        byteArraySize = dimension * 8
        if i % byteArraySize == byteArraySize - 1:
            try:
                TImageMatrix.append(byteArray)
            except:
                TImageMatrix = [byteArray]
            byteArray = []
    return TImageMatrix


def HenonEncryption(imageName, key):
    imageMatrix, dimensionX, dimensionY, color = getImageMatrix(imageName)
    transformationMatrix = genHenonMap(dimensionY, key)
    resultantMatrix = []
    for i in range(dimensionX):
        row = []
        for j in range(dimensionY):
            try:
                if color:
                    row.append(
                        tuple([ transformationMatrix[i][j] ^ x for x in imageMatrix[i][j] ]))
                else:
                    row.append(transformationMatrix[i][j] ^ imageMatrix[i][j])
            except:
                if color:
                    row = [tuple([ transformationMatrix[i][j] ^ x for x in imageMatrix[i][j] ])]
                else:
                    row = [ transformationMatrix[i][j] ^ x for x in imageMatrix[i][j] ]
        try:
            resultantMatrix.append(row)
        except:
            resultantMatrix = [row]
    if color:
        im = Image.new("RGB", (dimensionX, dimensionY))
    else:
        im = Image.new(
            "L", (dimensionX, dimensionY))  # L is for Black and white pixels

    pix = im.load()
    for x in range(dimensionX):
        for y in range(dimensionY):
            pix[x, y] = resultantMatrix[x][y]
    im.save(imageName.split('.')[0] + "_HenonEnc.png", "PNG")


def HenonDecryption(imageNameEnc, key):
    imageMatrix, dimensionX, dimensionY, color = getImageMatrix(imageNameEnc)
    transformationMatrix = genHenonMap(dimensionY, key)
    pil_im = Image.open(imageNameEnc, 'r')
    imshow(np.asarray(pil_im))
    henonDecryptedImage = []
    for i in range(dimensionX):
        row = []
        for j in range(dimensionY):
            try:
                if color:
                    row.append(
                        tuple([ transformationMatrix[i][j] ^ x for x in imageMatrix[i][j] ]))
                else:
                    row.append(transformationMatrix[i][j] ^ imageMatrix[i][j])
            except:
                if color:
                    row = [tuple([ transformationMatrix[i][j] ^ x for x in imageMatrix[i][j] ])]
                else:
                    row = [ transformationMatrix[i][j] ^ x for x in imageMatrix[i][j] ]
        try:
            henonDecryptedImage.append(row)
        except:
            henonDecryptedImage = [row]
    if color:
        im = Image.new("RGB", (dimensionX, dimensionY))
    else:
        im = Image.new(
            "L", (dimensionX, dimensionY))  # L is for Black and white pixels

    pix = im.load()
    for x in range(dimensionX):
        for y in range(dimensionY):
            pix[x, y] = henonDecryptedImage[x][y]
    im.save(imageNameEnc.split('_')[0] + "_HenonDec.png", "PNG")


if __name__ == '__main__':
    key = (0.1, 0.1)
    HenonEncryption("img/lena.jpg", key)
    img = cv2.imread("img/lena_HenonEnc.png", cv2.IMREAD_COLOR)
    cv2.imshow("image", img)
    cv2.waitKey()

    # HenonDecryption("img/lena_HenonEnc.png", key)
