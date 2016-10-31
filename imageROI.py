import cv2
import sys
from PyQt5.QtGui import *
import PyQt5.QtWidgets
# from PyQt5.QtGui.QPixmap
import numpy as np

img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg')
print type(img)
print img.shape
print img.dtype
print np.dtype('uint16').itemsize

# bitmap = cv2.cv.CreateImageHeader((img.shape[1],img.shape[0]),cv2.cv.IPL_DEPTH_8U,3)
bitmap = cv2.cv.CreateImage((img.shape[1],img.shape[0]),cv2.cv.IPL_DEPTH_8U,3)
print type(bitmap)
cv2.cv.SetData(bitmap,img.tostring(),img.dtype.itemsize*3*img.shape[1])
print type(bitmap)

cv2.cv.NamedWindow('image',cv2.cv.CV_WINDOW_FULLSCREEN)
cv2.cv.ShowImage('image',bitmap)
cv2.cv.WaitKey(0)

cv2.cv.SetImageROI(bitmap,(100,200,400,500))

cv2.cv.ShowImage('image',bitmap)
cv2.cv.WaitKey(0)
