import cv2
import numpy as np

img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg',cv2.IMREAD_COLOR)



print type(img),img.shape

mat = np.mat([[255,100,10],[100,50,200]])
print type(mat)
# cv2.imshow('img',mat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print img2gray.shape
print type(img2gray)
print img2gray[:10,:10]
ret, mask = cv2.threshold(img2gray[:10,:10], 70, 255, cv2.THRESH_BINARY)
print ret
print mask

mask_inv = cv2.bitwise_not(mask)
print mask_inv

img1_bg = cv2.bitwise_and(img2gray[:10,:10],img2gray[:10,:10],mask = mask_inv)
print img1_bg