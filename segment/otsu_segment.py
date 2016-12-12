# coding=utf-8
import cv2
import numpy as np

image = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')

image = cv2.resize(image,(500,400))

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

# 计算图像直方图
hist = cv2.calcHist(gray, [0], None, [256], [0, 256])
rows,cols = gray.shape

# 直方图归一化
hist /= float(hist.sum())

omega = np.zeros((256,), dtype='float64')
mu = np.zeros((256,), dtype='float64')

omega[0] = hist[0]
mu[0] = hist[0]

for i in range(1,256):
    omega[i] = omega[i-1] + hist[i]
    mu[i] = mu[i-1] + (i * hist[i])

mean = mu[255]
max_value = 0
k_max = 0

for k in range(1,255):
    PA = omega[k]
    PB = 1 - omega[k]
    v = 0
    if (PA > 0.001) & (PB > 0.001):
        MA = mu[k] / PA
        MB = (mean - mu[k]) / PB
        value = PA * (MA - mean) * (MA - mean) + PB * (MB - mean) * (MB - mean)
        if value > max_value:
            max_value = value
            k_max = k

print k_max

ret,thresh = cv2.threshold(gray,k_max,255,cv2.THRESH_BINARY)

cv2.imshow('thresh',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()