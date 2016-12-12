# coding=utf-8
import cv2
import numpy as np

k_clusters = 2

image = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg')
image = cv2.resize(image,(500,400))

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('gray',gray)

nums_cluster = np.ones((k_clusters,))
centers = np.ones((k_clusters,), dtype='float64')
clusters = {}

kmeans = gray.copy()
seen = set([])
# 随机初始化聚类中心
for i in range(k_clusters):
    v = np.random.choice(list(range(255)))
    while v in seen:
        v = np.random.choice(list(range(255)))
    seen.add(v)
    centers[i] = v
    clusters[i] = [v]
rows, cols = gray.shape

flag = True
while flag:
    for r in range(rows):
        for c in range(cols):
            pixel = gray[r, c]
            #  计算该像素点到各个聚类中心的距离，并将该点划分到与之最近的聚类
            min = np.argmin((centers - pixel) ** 2)
            nums_cluster[min] += 1
            clusters[min].append(pixel)

    # 重新计算聚类中心，新聚类中心与愿聚类中心为同一像素值或两者之差小于某一阈值则停止计算
    flag = False
    for i in range(k_clusters):
        new_center = int(sum(clusters[i])/nums_cluster[i])
        print 'new cener :', i ,centers[i] ,new_center,(centers[i] - new_center)
        if (centers[i] == new_center) | (abs((centers[i] - new_center)) < 1):
            centers[i] = new_center
        else:
            flag = True
            centers[i] = new_center
    print '     ------------------   '

print 'end loop ........'

for r in range(rows):
    for c in range(cols):
        pixel = gray[r, c]
        min_dis = np.argmin((centers - pixel) ** 2)
        kmeans[r,c] = centers[min_dis]

cv2.imshow('kmeans',kmeans)

ret,mask = cv2.threshold(kmeans,100,255,cv2.THRESH_BINARY)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()