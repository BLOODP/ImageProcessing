# coding=utf-8
import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

g = np.array([[1,2,1],[2,4,2],[1,2,1]])  #高斯核

rows,cols = img_gray.shape
avg33 = img_gray.copy()
# avg55 =  img_gray.copy()
gaussian = img_gray.copy()
print "starting"
for r in range(1,rows-1):
    # row1 = img_gray[r-1:]
    for c in range(1,cols-1):
        avg33[r, c] = np.sum(img_gray[r-1:r+2,c-1:c+2])/9
        # avg55[r, c] = np.sum(img[r - 2:r + 2, c - 2:c + 2]) / 25
        gaussian[r,c] = np.sum(np.multiply(img_gray[r-1:r+2,c-1:c+2], g)) / 16

print "end"

cv2.imshow("gray",img_gray)
cv2.imshow("averaging 3*3",avg33)
cv2.imshow("gaussian 3*3",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
