import numpy as np
import cv2

img = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')
img = cv2.resize(img,(700,400))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_img',gray_img)

rows,cols = gray_img.shape
mask = np.zeros_like(gray_img,dtype='uint8')

print 'staring ............'
gx = np.array([[1,0],[0,-1]],dtype='int8')
gy = np.array([[0,1],[-1,0]],dtype='int8')
for r in range(rows-1):
    for c in range(1,cols-1):
        Gx = np.sum(np.array(gray_img[r :r + 2, c :c + 2]) * gx)
        Gy = np.sum(np.array(gray_img[r :r + 2, c :c + 2]) * gy)
        mask[r,c] = abs(Gx) + abs(Gy)
        print abs(Gx) + abs(Gy)

cv2.imshow('mask',mask)


ret,thresh = cv2.threshold(mask,50,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()