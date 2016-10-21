import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows,cols = img_gray.shape
minimum =  img_gray.copy()

print "starting"
for r in range(1,rows-1):
    # row1 = img_gray[r-1:]
    # row2 = img_gray[r:]
    # row3 = img_gray[r+1:]
    for c in range(1,cols-1):
        # img_gray[r,c] = (row1[c-1]+row1[c]+row1[c+1]+row2[c-1]+row2[c]+row2[c+1+row3[c-1]+row3[c]+row3[c+1])/9
        minimum[r, c] = img_gray[r-1:r+2,c-1:c+2].min()



print "end"

cv2.imshow("gray",img_gray)
cv2.imshow("minimum 3*3",minimum)
# cv2.imshow("averaging 5*5",avg55)
cv2.waitKey(0)
cv2.destroyAllWindows()
