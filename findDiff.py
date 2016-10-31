# coding=utf-8
import cv2
import numpy as np

# 读取彩色图片
origin = cv2.imread('/Users/heguangqin/Pictures/diff1.png')

#   将彩色图片转换为灰度图
img = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("origin image", cv2.WINDOW_NORMAL)
cv2.namedWindow("thresh1", cv2.WINDOW_NORMAL)
cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)

cv2.imshow("origin image", origin)

# 将原图切分为两幅相同大小的图片，并且像素点对应，但这里处理比较粗糙：
# 直接将原图的前567列切为图片一，后567列划为图片二
width = img.shape[1]
nw = int(width / 2)

# 由于原图片为uint8类型，如果这样直接将两张图片相减，将不会存在小于0的数，
# 即如果一个小的像素值减去一个大的像素值会得到一个较大的正像素值，如 100-102=254
# 所以应该将img1,img2转换为 'ing64' 即有符号64位而不能转换为有符号8位
img1 = img[:, :567]
print "image1 dtype : ", img1.dtype
img1_64 = np.array(img1.tolist(), dtype='int64')
print "img1_64 dtype : ", img1_64.dtype

img2 = img[:, 569:]
img2_64 = np.array(img2.tolist(), dtype='int64')
print "img2_64", img2_64.dtype

# 将两图相减，由于两图都是numpy 的数组，可直接相减
sub = img2_64 - img1_64
print 'sub:', sub.dtype
mask = np.absolute(sub)  # 取绝对值，将负数取正

# 将mask转换为 uint8 类型
mask = np.array(mask.tolist(), dtype='uint8')
print 'mask:', mask.dtype
print 'sub:', sub.shape
print np.sum(mask < 0, 0)  # 检验是否仍有小于0的像素值

print img.shape
print img1.shape
print img2.shape

# 二值化处理，改变像素值小于40的像素点为0像素值，大于40的变为255像素值
ret, thresh1 = cv2.threshold(mask, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("th", thresh1)

# 降噪处理，如果一个像素周围的90个像素中，像素值为255的比率小于0.2
# 则认为该像素点为噪声，将其像素值设为0
for i in range(15, thresh1.shape[0] - 15):
    for j in range(15, thresh1.shape[1] - 15):
        mas = thresh1[i - 15:i + 15, j - 15:j + 15]
        r = float(np.sum(mas == 255)) / float(np.sum(mas >= 0))
        if r < 0.2:
            thresh1[i, j] = 0
            print r
    thresh1[:, :15] = 0
    thresh1[:, -15:] = 0
    thresh1[:15, :] = 0
    thresh1[-15:, :] = 0

cv2.imshow("thresh1", thresh1)

#  使用核将白色区域扩大
kernel = np.ones((5, 5), np.uint8)
thresh1 = cv2.dilate(thresh1, kernel, iterations=1)
cv2.imshow("mask", thresh1)

# 边缘检测，画出不同出的边缘
thresh = cv2.Canny(thresh1, 240, 250, apertureSize=3)
cv2.imshow("thresh", thresh)

# 画出边线
origin[thresh == 255] = (0, 0, 255)
origin[:, 569:][(thresh == 255)] = (0, 0, 255)

cv2.imshow("res", origin)

cv2.waitKey(0)
cv2.destroyAllWindows()
