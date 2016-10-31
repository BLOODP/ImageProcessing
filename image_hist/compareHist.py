import cv2
import numpy as np

image1 = cv2.cv.LoadImage("/Users/heguangqin/Pictures/source_1.jpg")
image2 = cv2.cv.LoadImage("/Users/heguangqin/Pictures/fengche.jpg")
image3 = cv2.cv.LoadImage("/Users/heguangqin/Pictures/source_1.jpg")

hist_size = 256

gray_plane1 = cv2.cv.CreateImage(cv2.cv.GetSize(image1),8,1)
cv2.cv.CvtColor(image1,gray_plane1,cv2.cv.CV_BGR2GRAY)
gray_hist1 = cv2.cv.CreateHist([256],cv2.cv.CV_HIST_ARRAY,[[0,255]],1)
cv2.cv.CalcHist([gray_plane1],gray_hist1)

gray_plane2 = cv2.cv.CreateImage(cv2.cv.GetSize(image2),8,1)
cv2.cv.CvtColor(image2,gray_plane2,cv2.cv.CV_BGR2GRAY)
gray_hist2 = cv2.cv.CreateHist([256],cv2.cv.CV_HIST_ARRAY,[[0,255]],1)
cv2.cv.CalcHist([gray_plane2],gray_hist2)

gray_plane3 = cv2.cv.CreateImage(cv2.cv.GetSize(image3),8,1)
cv2.cv.CvtColor(image1,gray_plane3,cv2.cv.CV_BGR2GRAY)
gray_hist3 = cv2.cv.CreateHist([256],cv2.cv.CV_HIST_ARRAY,[[0,255]],1)
cv2.cv.CalcHist([gray_plane3],gray_hist3)

com1 = cv2.cv.CompareHist(gray_hist1,gray_hist2,cv2.cv.CV_COMP_BHATTACHARYYA)
print 'compare image1 with image2:',com1
com2 = cv2.cv.CompareHist(gray_hist1,gray_hist3,cv2.cv.CV_COMP_BHATTACHARYYA)
print 'compare image1 with image3:',com2
com3 = cv2.cv.CompareHist(gray_hist2,gray_hist3,cv2.cv.CV_COMP_BHATTACHARYYA)
print 'compare image2 with image3:',com3


# cv2.cv.NormalizeHist(gray_hist1,1.0)
# bins = gray_hist1.bins
# minV, maxV, minloc, maxloc = cv2.cv.MinMaxLoc(bins)
# print minV, maxV, minloc, maxloc
# print cv2.cv.QueryHistValue_1D(gray_hist1,100)
