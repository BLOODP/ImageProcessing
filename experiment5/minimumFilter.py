import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows,cols = img_gray.shape
minimum =  img_gray.copy()

print "starting"
for r in range(1,rows-1):
    for c in range(1,cols-1):
        minimum[r, c] = img_gray[r-1:r+2,c-1:c+2].min()
print "end"

cv2.imshow("gray",img_gray)
cv2.imshow("minimum 3*3",minimum)
cv2.waitKey(0)
cv2.destroyAllWindows()


