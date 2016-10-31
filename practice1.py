import numpy as np
import cv2

img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg',cv2.IMREAD_COLOR)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
print img.shape
timeSpent = cv2.getTickCount()

tempimg1 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print 'temp img1 ',tempimg1.shape
tempimg2 = cv2.cvtColor(tempimg1,cv2.COLOR_GRAY2RGB)
print 'temp img2 ',tempimg2.shape

for i in range(100):
    blender = float(i/100.0)
    print blender
    dstimg = cv2.addWeighted(img,blender,tempimg2,(1-blender),0)
    cv2.imshow('image',dstimg)
    cv2.waitKey(30)

timeSpent = (cv2.getTickCount()-timeSpent)/cv2.getTickFrequency()
print 'Time spent in milliseconds:',timeSpent*1000

cv2.waitKey(0)
cv2.destroyAllWindows()