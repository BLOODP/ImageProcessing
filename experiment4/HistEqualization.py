import cv2
import numpy as np

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg")
# cv2.namedWindow("blue",cv2.WINDOW_NORMAL)

img_b, img_g, img_r = cv2.split(img)

equ_b = cv2.equalizeHist(img_b)
equ_g = cv2.equalizeHist(img_g)
equ_r = cv2.equalizeHist(img_r)

equ = cv2.merge([equ_b,equ_g,equ_r])

cv2.imshow("blue", img)
cv2.imshow("equ", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
