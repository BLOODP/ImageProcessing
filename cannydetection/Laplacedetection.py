import numpy as np
import cv2

gx = np.array([[-1,-1,-1],[0,0,0],[-1,-1,-1]],dtype='int8')
gy = np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype='int8')
laplace = np.array([[0,1,0],[1,-4,1],[0,1,0]],dtype='int8')

img = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')
img = cv2.resize(img,(400,300))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_img',gray_img)

rows,cols = gray_img.shape
mask = np.zeros_like(gray_img,dtype='uint8')

print 'staring ............'
# for r in range(1,rows-1):
#     for c in range(1,cols-1):
#         # Gx = np.sum(np.array(gray_img[r - 1:r + 2, c - 1:c + 2]) * gx)
#         # Gy = np.sum(np.array(gray_img[r - 1:r + 2, c - 1:c + 2]) * gy)
#         # mask[r,c] = abs(Gx) + abs(Gy)
#         g = np.sum(np.multiply(np.array(gray_img[r - 1:r + 2, c - 1:c + 2]), laplace))
#         mask[r,c] = abs(g)
#         # print np.sum(np.array(gray_img[r - 1:r + 2, c - 1:c + 2]) * laplace)
#         print g
#
# cv2.imshow('mask',mask)
#
# print mask[100:110,100:110]
#
# ret,thresh = cv2.threshold(mask,200,255,cv2.THRESH_BINARY)
# cv2.imshow('thresh',thresh)

lap = cv2.Laplacian(gray_img,cv2.CV_8U,ksize=3)
cv2.imshow('lap',lap)

ret,thresh = cv2.threshold(lap,150,255,cv2.THRESH_BINARY)
cv2.imshow('thresh1',thresh)

gimg = cv2.GaussianBlur(img,(3,3),0,borderType=cv2.BOOST_DEFAULT)
cv2.imshow('gimg',gimg)
cv2.imshow('img',img)

gimg_gray = cv2.cvtColor(gimg,cv2.COLOR_BGR2GRAY)
cv2.imshow('gimg_gray',gimg_gray)

lapg = cv2.Laplacian(gimg_gray,cv2.CV_8U,ksize=3)
cv2.imshow('lapg',lapg)

ret,thresh2 = cv2.threshold(lapg,40,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh2',thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()