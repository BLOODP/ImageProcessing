# coding=utf-8
import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

lap = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype='int32')  #拉普拉斯核
print lap.dtype

rows,cols = img_gray.shape
avg33 = img_gray.copy()
# avg55 =  img_gray.copy()
sharpe = np.zeros_like(img_gray)
print sharpe.dtype

print "starting"
for r in range(1,rows-1):
    # row1 = img_gray[r-1:]
    for c in range(1,cols-1):
        avg33[r, c] = np.sum(img_gray[r-1:r+2,c-1:c+2])/9
        # avg55[r, c] = np.sum(img[r - 2:r + 2, c - 2:c + 2]) / 25
        sharpe[r,c] = np.sum(np.multiply(img_gray[r-1:r+2,c-1:c+2], lap))/5

print "end"
print sharpe.dtype

cv2.imshow("gray",img_gray)
cv2.imshow("averaging 3*3",avg33)
cv2.imshow("sharp 3*3",sharpe)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.cv.CreateImage()
