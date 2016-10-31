import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows,cols = img_gray.shape
avg33 = img_gray.copy()
avg55 = img_gray.copy()
print "starting"
for r in range(1,rows-1):
    for c in range(1,cols-1):
        avg33[r, c] = np.sum(img_gray[r-1:r+2,c-1:c+2])/9
        avg55[r, c] = np.sum(img_gray[r - 2:r + 3, c - 2:c + 3]) / 25

print "end"

cv2.imshow("gray",img_gray)
cv2.imshow("averaging 3*3",avg33)
cv2.imshow("averaging 5*5",avg55)
cv2.waitKey(0)
cv2.destroyAllWindows()
