# coding=utf-8
import numpy as np
import cv2

left = cv2.imread('/Users/heguangqin/Pictures/left.jpg')
left = left[10:-10,10:-10]
right = cv2.imread('/Users/heguangqin/Pictures/right.jpg')
right = right[10:-10,10:-10]

cv2.imshow('left',left)
cv2.imshow('right',right)

left_gray = cv2.cvtColor(left,cv2.COLOR_BGR2GRAY)
right_gray = cv2.cvtColor(right,cv2.COLOR_BGR2GRAY)

cv2.imshow('left_gray',left_gray)
cv2.imshow('right_gray',right_gray)

surf = cv2.SURF(400)

#     分别检测特征点并生成描述
left_kp, left_des = surf.detectAndCompute(left_gray,None)
right_kp, right_des = surf.detectAndCompute(right_gray,None)
print '------------- the length of keypoints------'
print len(left_kp),len(right_kp)
print

print '-------------- flann features matching -----'
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(left_des,right_des,k=2)
print 'the length of matches : ', len(matches)

print 'picking good matches....'
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
print 'the length of good matches : ', len(good)

src_pts = np.float32([left_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
dst_pts = np.float32([right_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

#   获取左边图像到右边图像的投影映射关系
M,mask = cv2.findHomography(src_pts,dst_pts,cv2.RANSAC, 5.0)

#  将左图通过透视变换映射到右图
left_on_right = cv2.warpPerspective(left_gray,M,(right_gray.shape[1],right_gray.shape[0]))
cv2.imshow('left_on_right',left_on_right)

#   得到左图的四个顶点经过变换后的目标点
h, w = left_gray.shape
pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1, 1, 2)
dst = cv2.perspectiveTransform(pts,M)
lh,lw = right_gray.shape
print 'lh : ',lh, 'lw : ', lw
print 'the dst points : ', np.int32(dst)
print 'the min and max : ', np.int32(dst)[:,0,0].min(),np.int32(dst)[:,0,1].min()

#  得到目标点后，发现右边两个顶点可能会超出表示范围，需要通过平移将这四个点的位置改变
wt = abs(np.int32(dst)[:,0,0].min()) if np.int32(dst)[:,0,0].min() < 0 else 0
ht = abs(np.int32(dst)[:,0,1].min()) if np.int32(dst)[:,0,1].min() < 0 else 0

dst = np.int32(dst).reshape(-1,2) + [wt,ht]
print 'changed dst : ',dst
print

#   得到目标点后通过getPerspectiveTransform得到左图四个顶点到改变后的目标点的变换公式
M = cv2.getPerspectiveTransform(np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]),np.float32(dst))
#    通过得到的变换公式完成左图的透视变换
left_warp = cv2.warpPerspective(left_gray,M,(dst[:,0].max(),dst[:,1].max()))
left_warp_color = cv2.warpPerspective(left,M,(dst[:,0].max(),dst[:,1].max()))
cv2.imshow('left_warp',left_warp)
cv2.imshow('left_warp_color',left_warp_color)

print '------------ strip the left_warp --------------'
stripped = left_warp[ht:ht+lh,:]
stripped_color = left_warp_color[ht:ht+lh,:]
print 'the stripped shape : ', stripped.shape
cv2.imshow('stripped',stripped)
cv2.imshow('stripped_color',stripped_color)

print
print '-------------- joint --------------------------'
sl = np.zeros((lh,lw+wt),dtype='uint8')
sl_color = np.zeros((lh,lw+wt,3),dtype='uint8')
sr = np.zeros((lh,lw+wt),dtype='uint8')
sr_color = np.zeros((lh,lw+wt,3),dtype='uint8')
sl[:,:stripped.shape[1]] = stripped
sl_color[:,:stripped_color.shape[1]] = stripped_color

# 二值化处理
ret,thresh1 = cv2.threshold(left_on_right,1,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh',thresh1)


bit_and = cv2.bitwise_and(right_gray,right_gray,mask=thresh1)
bit_and_color = cv2.bitwise_and(right,right,mask=thresh1)
cv2.imshow('bit_and',bit_and)
cv2.imshow('bit_and_color',bit_and_color)
print 'the bit_and shape : ', bit_and.shape
sr[:,-lw:] = bit_and
sr_color[:,-lw:] = bit_and_color

cv2.imshow('sr',sr)
cv2.imshow('sl',sl)
cv2.imshow('sl_color',sl_color)
cv2.imshow('sr_color',sr_color)
# 将两张图片拼接
ss = cv2.add(sl,sr)
cv2.imshow('ss',ss)

ss_color = cv2.add(sl_color,sr_color)
print 'ssc shape : ', ss_color.shape
cv2.imshow('ss color',ss_color)

cv2.waitKey(0)
cv2.destroyAllWindows()