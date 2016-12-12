# coding=utf-8
import cv2
import numpy as np


#   高斯低通核
def gaussianLowFilter():
    D0 = float(2 * 50 * 50)
    gaussian = np.zeros((image_gray.shape[0], image_gray.shape[1], 2), dtype='float32')
    for i in range(oph):
        for j in range(opw):
            d = float(pow(i - oph / 2, 2) + pow(j - opw / 2, 2))
            gaussian[i, j][0] = np.exp(-d / D0)
            gaussian[i, j][1] = np.exp(-d / D0)
        print 'd , exp : ', d, np.exp(-d / D0)
    return gaussian


# 高斯高通核
def gaussianHighFilter():
    D0 = float(2 * 50 * 50)
    gaussian = np.zeros((image_gray.shape[0], image_gray.shape[1], 2), dtype='float32')
    for i in range(oph):
        for j in range(opw):
            d = float(pow(i - oph / 2, 2) + pow(j - opw / 2, 2))
            gaussian[i, j][0] = 1 - np.exp(-d / D0)
            gaussian[i, j][1] = 1 - np.exp(-d / D0)
        print 'd , exp : ', d, np.exp(-d / D0)
    return gaussian


# 理想低通核
def idealLowFilter():
    D0 = float(2 * 50 * 50)
    gaussian = np.zeros((image_gray.shape[0], image_gray.shape[1], 2), dtype='float32')
    for i in range(oph):
        for j in range(opw):
            d = float(pow(i - oph / 2, 2) + pow(j - opw / 2, 2))
            gaussian[i, j][0] = 1 if d <= D0 else 0
            gaussian[i, j][1] = 1 if d <= D0 else 0
        print 'd , exp : ', d, 1 if d <= D0 else 0
    return gaussian


def idealHighFilter():
    D0 = float(2 * 50 * 50)
    gaussian = np.zeros((image_gray.shape[0], image_gray.shape[1], 2), dtype='float32')
    for i in range(oph):
        for j in range(opw):
            d = float(pow(i - oph / 2, 2) + pow(j - opw / 2, 2))
            gaussian[i, j][0] = 0 if d <= D0 else 1
            gaussian[i, j][1] = 0 if d <= D0 else 1
            print 'd , exp : ', d, 0 if d <= D0 else 1
    return gaussian


#   巴特斯沃低通核
def buttersworthLowFilter():
    D0 = float(2 * 50 * 50)
    gaussian = np.zeros((image_gray.shape[0], image_gray.shape[1], 2), dtype='float32')
    for i in range(oph):
        for j in range(opw):
            d = float(pow(i - oph / 2, 2) + pow(j - opw / 2, 2))
            gaussian[i, j][0] = 1 / (1 + pow((d / D0), 2))
            gaussian[i, j][1] = 1 / (1 + pow((d / D0), 2))
            print 'd , exp : ', d, 1 / (1 + pow((d / D0), 2))
    return gaussian

def buttersworthHighFilter():
    D0 = float(2 * 50 * 50)
    gaussian = np.zeros((image_gray.shape[0], image_gray.shape[1], 2), dtype='float32')
    for i in range(oph):
        for j in range(opw):
            d = float(pow(i - oph / 2, 2) + pow(j - opw / 2, 2))
            gaussian[i, j][0] = 1 - (1 / (1 + pow((d / D0), 2)))
            gaussian[i, j][1] = 1 - (1 / (1 + pow((d / D0), 2)))
            print 'd , exp : ', d, 1 - (1 / (1 + pow((d / D0), 2)))
    return gaussian


image = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')
image = cv2.resize(image, (800, 600))
cv2.imshow('image', image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale_image', image_gray)
image_gray = np.array(image_gray.tolist(), dtype='float32')

# 中心化
for i in range(image_gray.shape[0]):
    for j in range(image_gray.shape[1]):
        image_gray[i, j] *= pow(-1, (i + j))

# ---------------  手动实现二维基本傅立叶变换 （速度非常慢即效率低）
#
# dftRe = np.zeros(image_gray.shape, dtype='float32')
# dftIm = np.zeros(image_gray.shape, dtype='float32')
#
# Pi2 = 2 * 3.141592654
# i = 0
# j = 0
# k = 0
# print 'loop start'
# for u in range(image_gray.shape[0]):
#     for v in range(image_gray.shape[1]):
#         sinDft = 0
#         cosDft = 0
#         for i in range(image_gray.shape[0]):
#             for j in range(image_gray.shape[1]):
#                 temp = Pi2 * (float((u * i)) / float(image_gray.shape[0]) + float((v * j)) / float(image_gray.shape[1]))
#                 sinDft -= float(image_gray[i, j]) * float(np.sin(temp))
#                 cosDft += image_gray[i, j] * float(np.cos(temp))
#                 k += 1
#             print 'k : ', k, sinDft, cosDft
#         dftRe[u, v] = sinDft
#         dftIm[u, v] = cosDft
#
# print 'end loop'
#
# dftRe = cv2.divide(dftRe, image_gray.shape[0] * image_gray.shape[1])
# dftIm = cv2.divide(dftIm, image_gray.shape[0] * image_gray.shape[1])
# dftRe = cv2.multiply(dftRe, dftRe)
# dftIm = cv2.multiply(dftIm, dftIm)
# dftRe = cv2.add(dftRe, dftIm)
# dftRe = cv2.pow(dftRe, 0.5)
# print 'dftRe dtype', dftRe.dtype
# print 'dft '
# print dftRe[0, :20]
# cv2.imshow('dftRe', dftRe)
# print dftRe.shape

# ------------- 使用 opencv 快速傅立叶变换 （速度快，效率高）建议使用opencv 快速傅立叶变换

oph = cv2.getOptimalDFTSize(image_gray.shape[0])
opw = cv2.getOptimalDFTSize(image_gray.shape[1])
padded = cv2.copyMakeBorder(image_gray, 0, oph - image_gray.shape[0], 0, opw - image_gray.shape[1], cv2.BORDER_CONSTANT,
                            value=0)
temp = [padded, np.zeros(image_gray.shape, dtype='float32')]
complexl = cv2.merge(temp)

#   傅立叶变换
cv2.dft(complexl, complexl)
cv2.split(complexl, temp)

#    显示频谱图
aa = cv2.magnitude(temp[0], temp[1])
aa = cv2.divide(aa, opw * oph)
cv2.imshow('aa', aa)

# gaussian = gaussianLowFilter()
# gaussian = gaussianHighFilter()
# gaussian = idealLowFilter()
# gaussian = idealHighFilter()
# gaussian = buttersworthHighFilter()
gaussian = buttersworthLowFilter()

#   频率过滤
gaussian = cv2.multiply(complexl, gaussian)
cv2.split(gaussian, temp)

#     显示频率过滤之后的频谱图
bb = cv2.magnitude(temp[0], temp[1])
bb = cv2.divide(bb, opw * oph)
cv2.imshow('bb', bb)
print gaussian.shape

#     傅立叶反变换
cv2.dft(gaussian, gaussian, cv2.DFT_INVERSE)

dstBlur = cv2.split(gaussian)
for i in range(oph):
    for j in range(opw):
        dstBlur[0][i, j] *= pow(-1, i + j)

cv2.normalize(dstBlur[0], dstBlur[0], 1, 0, cv2.NORM_MINMAX)
cv2.imshow('dstBlur', dstBlur[0])

cv2.waitKey(0)
cv2.destroyAllWindows()
