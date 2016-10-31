import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows,cols = img_gray.shape
maximum = img_gray.copy()

print "starting"
for r in range(1,rows):
    for c in range(1,cols):
        maximum[r, c] = np.max(img_gray[r-1:r+1,c-1:c+1])


print "end"

cv2.imshow("gray",img_gray)
cv2.imshow("maximum 3*3",maximum)
# cv2.imshow("averaging 5*5",avg55)
cv2.waitKey(0)
cv2.destroyAllWindows()
