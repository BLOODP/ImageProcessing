# coding=utf-8
import cv2
import numpy as np

# 读取彩色图片
origin = cv2.imread('/Users/heguangqin/Pictures/diff2.jpg')
print origin.shape

#   将彩色图片转换为灰度图
img = cv2.cvtColor(origin,cv2.COLOR_BGR2GRAY)

# for i in range(img.shape[1]):
#     col = np.all(img[:,i]==255)
#     print col
cols = [ i for i in range(img.shape[1]) if np.all(img[400:,i]==255)]
print 'cols :',cols

#
# cv2.namedWindow("origin image",cv2.WINDOW_NORMAL)
# cv2.namedWindow("thresh1",cv2.WINDOW_NORMAL)
# cv2.namedWindow("thresh",cv2.WINDOW_NORMAL)

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

# dst = cv2.addWeighted(img1_canny,0.5,img2_canny,0.5,0)
# cv2.imshow("dst",dst)

# ret,th = cv2.threshold(dst,200,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("th",th)

# sub = img2_64 - img1_64
# print 'sub:',sub.dtype
# mask = np.absolute(sub)

#将mask转换为 uint8 类型
# mask = np.array(mask.tolist(),dtype='uint8')
# cv2.imshow("mask",mask)
# print 'mask:',mask.dtype
# print 'sub:',sub.shape
# print np.sum(mask<0,0)  # 检验是否仍有小于0的像素值



cv2.waitKey(0)
cv2.destroyAllWindows()