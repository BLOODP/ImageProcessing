import numpy as np
import cv2

image = cv2.imread('/Users/heguangqin/Pictures/fengche.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# corners = cv2.goodFeaturesToTrack(gray,400,0.01,10)
# print len(corners)
# corners = np.int0(corners)
# for i in corners:
#     x,y = i.ravel()
#     print x,y
#     cv2.circle(image, (x, y), 3, 255, -1)

# sift = cv2.SIFT()
# kp = sift.detect(image,None)
# print type(kp)
# print type(kp[0]),len(kp)
# print dir(kp[0])
# print kp[0].pt,kp[0].angle,kp[0].size
#
# img=cv2.drawKeypoints(image,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# kp,des = sift.compute(image,kp)
# print type(des),len(des),des.shape
# print des[0]

# surf = cv2.SURF(5000)
# surf.upright = True
# kp, des = surf.detectAndCompute(image,None)


# fast = cv2.FastFeatureDetector()
# kp = fast.detect(image,None)
#
# # print type(kp),len(kp),
# img=cv2.drawKeypoints(image,kp,color=(255,0,0))
# print "Threshold: ", fast.getInt('threshold')
# print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
# # print "neighborhood: ", fast.getInt('type')
# print "Total Keypoints with nonmaxSuppression: ", len(kp)

# star = cv2.FeatureDetector_create("STAR")
# brief = cv2.DescriptorExtractor_create("BRIEF")
# kp = star.detect(image,None)
# kp, des = brief.compute(image, kp)

orb = cv2.ORB()
kp = orb.detect(image,None)
kp, des = orb.compute(image, kp)

img=cv2.drawKeypoints(image,kp,color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()