import numpy as np
import cv2

image = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')
rows,cols,c = image.shape
print image.shape

# M = np.float32([[1,0,100],[0,1,50]])
# M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# pts1 = np.float32([[10,10],[20,10],[10,20]])
# pts2 = np.float32([[10,10],[20,20],[10,0]])
# M = cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(image,M,(rows,cols))

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)

print M
dst = cv2.warpPerspective(image,M,(cols,rows))
print dst.shape
cv2.imshow('img',image)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()