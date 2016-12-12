# coding=utf-8
import cv2
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', ['x','y'])
neighbors = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), Point(0, 1), Point(-1, 1), Point(-1, 0)]

image = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')

image = cv2.resize(image,(500,400))

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
gray_int32 = np.array(gray.tolist(),dtype='int32')

#   对灰度图做二值化处理
ret, thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)

flag_mat = np.zeros_like(gray)
res = np.zeros_like(gray)

#   从二值图像中随机选取100个值为255的像素点
w = np.where(thresh == 255)
z = list(zip(w[0].tolist(), w[1].tolist()))

length = len(z)
r = list(np.random.choice(np.arange(int(length/20)), 5))
for i in range(2,20):
    r.extend(list(np.random.choice(np.arange(int(length/20)*(i-1),int(length/20)*i), 5)))
print 'r : ',r

seeds = []
for index in r:
    seed = z[index]
    seeds.append(Point(seed[1], seed[0]))
    res[seed[0], seed[1]] = 255


# 区域生长
while seeds:
    seed = seeds.pop()
    flag_mat[seed.y, seed.x] = 1

    for i in range(8):
        tmpx = seed.x + neighbors[i].x
        tmpy = seed.y + neighbors[i].y

        if (tmpx < 0) | (tmpy < 0) | (tmpx >= 500) | (tmpy >= 400):
            continue
        if (flag_mat[tmpy, tmpx] != 1) and (abs(gray_int32[tmpy, tmpx] - gray_int32[seed.y, seed.x]) < 8):
            res[tmpy, tmpx] = 255
            flag_mat[tmpy, tmpx] = 1
            seeds.append(Point(tmpx, tmpy))

print 'ok'
cv2.imshow('res',res)
print 'gray ', gray.shape

cv2.waitKey(0)
cv2.destroyAllWindows()
