# coding=utf-8
import numpy as np
import cv2



img = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')
print img.shape

img = cv2.resize(img,(700,400))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_img',gray_img)

rows,cols = gray_img.shape
mask = np.zeros_like(gray_img,dtype='uint8')

print 'staring ............'
gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype='int8')
gy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]],dtype='int8')

# for r in range(1,rows-1):
#     for c in range(1,cols-1):
#         Gx = np.sum(np.array(gray_img[r - 1:r + 2, c - 1:c + 2]) * gx)
#         Gy = np.sum(np.array(gray_img[r - 1:r + 2, c - 1:c + 2]) * gy)
#         mask[r,c] = abs(Gx) + abs(Gy)
#         print abs(Gx) + abs(Gy)

cv2.imshow('mask',mask)

# 高斯平滑操作
gimg = cv2.GaussianBlur(img,(5,5),0,borderType=cv2.BOOST_DEFAULT)
cv2.imshow('gimg',gimg)
grayg = cv2.cvtColor(gimg,cv2.COLOR_BGR2GRAY)

# Sobel算子卷积操作
grayg_x = cv2.Sobel(grayg,cv2.CV_16SC1,1,0,ksize=3)
grayg_y = cv2.Sobel(grayg,cv2.CV_16SC1,0,1,ksize=3)
cv2.imshow('grayg_x',np.array(np.absolute(grayg_x).tolist(),dtype='uint8'))
cv2.imshow('grayg_y',np.array(np.absolute(grayg_y).tolist(),dtype='uint8'))
grayg_xy = np.array((np.absolute(grayg_x) + np.absolute(grayg_y)).tolist(),dtype='uint8')
cv2.imshow('gtaygxy',grayg_xy)

ret,thresh2 = cv2.threshold(grayg_xy,100,255,cv2.THRESH_BINARY)
cv2.imshow('thresh2',thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()