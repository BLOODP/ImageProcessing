# coding=utf-8
import cv2
import numpy as np

# 读取彩色图片
origin = cv2.imread('/Users/heguangqin/Pictures/diff2.jpg')
print origin.shape

#   将彩色图片转换为灰度图
img = cv2.cvtColor(origin,cv2.COLOR_BGR2GRAY)

cols = [ i for i in range(img.shape[1]) if np.all(img[400:,i]==255)]
print 'cols :',cols


cv2.imshow("origin image",origin)


width = img.shape[1]
nw = int(width/2)

img1 = img[:,:nw]
cols1 = [ i for i in range(img1.shape[1]) if np.all(img1[400:500,i]!=255)]
img1 = img1[:,cols1]
print cols1
img1_canny = cv2.Canny(img1,100,200)
cv2.imshow("img1_canny",img1)
print img1.shape
print "image1 dtype : ",img1.dtype
img1_64 = np.array(img1_canny.tolist(),dtype='int64')
print "img1_64 dtype : ", img1_64.dtype

img2 = img[:,nw:]
cols2 = [ j for j in range(img2.shape[1]) if np.all(img2[400:500,j]!=255)]
img2 = img2[:,cols2]
print img2.shape
img2_canny = cv2.Canny(img2,100,200)
cv2.imshow("img2_canny",img2)
img2_64 = np.array(img2_canny.tolist(),dtype='int64')
print "img2_64" , img2_64.dtype

cv2.waitKey(0)
cv2.destroyAllWindows()