import numpy as np
import cv2

image1 = cv2.imread('/Users/heguangqin/Pictures/box.jpg',0)
image2 = cv2.imread('/Users/heguangqin/Pictures/box_in_scene.jpg',0)

cv2.imshow('image1',image1)
cv2.imshow('image2',image2)

sift = cv2.SIFT()
kp1, des1 = sift.detectAndCompute(image1,None)
print len(kp1)
kp2, des2 = sift.detectAndCompute(image2,None)
print len(kp2)

# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = bf.match(des1,des2)
# print len(matches)
# matches = sorted(matches, key = lambda x:x.distance)
# img3 = cv2.drawMatches(image1,kp1,image2,kp2,matches[:10], flags=2)
# cv2.imshow('image3',img3)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

print len(good)
if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()

    h, w = image1.shape
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)
    print 'dst : ',dst
    cv2.polylines(image2, [np.int32(dst)], True, 255, 3)

    cv2.imshow('img2',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()