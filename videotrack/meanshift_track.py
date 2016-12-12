# coding=utf-8
import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/heguangqin/Downloads/yilake.mp4')

# 取视频的第一帧
ret, frame = cap.read()
print frame.shape

cv2.rectangle(frame,(580,140),(640,280),255,2)
cv2.imshow('frame',frame)

# 设置窗口的初始位置
r, h, c, w = 140, 140, 580, 60
track_window = (c, r, w, h)

# 提取窗口
roi = frame[r:r + h, c:c + w]
cv2.imshow('rot',roi)

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 32., 32.)), np.array((180., 255., 255.)))

# 计算窗口直方图
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
# 归一化直方图
roi_hist = cv2.normalize(roi_hist, 0, 255, cv2.NORM_MINMAX)
cv2.waitKey(0)

# 设置终止条件
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

x, y, w, h = track_window
print (x, y), (x + w, y + h)

while 1:
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # 调用opencv meanshift
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # 画出最新的窗口位置
        x, y, w, h = track_window
        cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv2.imshow('img2', frame)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
            # else:
            # cv2.imwrite(chr(k) + ".jpg", frame)
    else:
        break
# cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
