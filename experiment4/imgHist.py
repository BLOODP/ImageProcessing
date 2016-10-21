import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/Users/heguangqin/Pictures/source_1.jpg",0)
# colors = ['b', 'g', 'r']

# for i, col in enumerate(colors):
#     hist = cv2.calcHist(img, [i], None, [256], [0, 256])
#     print hist
#     plt.plot(hist, color=col)
#     plt.xlim([0, 256])
# plt.show()

# plt.hist(img.ravel(),256,[0,256])
# plt.show()


hist = cv2.calcHist(img, [0], None, [256], [0, 256])
mask = np.ones((256,256*3,3))

print hist.shape

maxValue = hist[hist.argmax()]

print maxValue[0]

for i in range(256):
    h = hist[i]
    height = int(256 - round(h*256/maxValue))
    cv2.rectangle(mask, (i*3, 256), (i*3+2, height), (0, 0, 255), lineType=0, thickness=1)
    print height



cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()