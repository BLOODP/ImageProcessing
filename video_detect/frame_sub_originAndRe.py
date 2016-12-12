import cv2.cv as cv
import sys

capture = cv.CaptureFromFile('/Users/heguangqin/Downloads/yilake.mp4')
nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))

cv.NamedWindow('video',1)
cv.NamedWindow('background',1)
cv.NamedWindow('foreground',1)

cv.MoveWindow('video',50,0)
cv.MoveWindow('background',500,0)
cv.MoveWindow('foreground',900,0)

pBkImg = None
pFrImg = None
pBkMat = None
pFrMat = None
pFrameMat = None


if not capture:
    sys.exit(0)

FramesNum = 0
while FramesNum < 100:

    pFrame = cv.QueryFrame(capture)
    FramesNum += 1

    if FramesNum == 1:
        print FramesNum
        pBkImg = cv.CreateImage((pFrame.width, pFrame.height),cv.IPL_DEPTH_8U,1)
        pFrImg = cv.CreateImage((pFrame.width, pFrame.height), cv.IPL_DEPTH_8U, 1)

        pBkMat = cv.CreateMat(pFrame.height,pFrame.width,cv.CV_32FC1)
        pFrMat = cv.CreateMat(pFrame.height, pFrame.width, cv.CV_32FC1)
        pFrameMat = cv.CreateMat(pFrame.height, pFrame.width, cv.CV_32FC1)

        cv.CvtColor(pFrame, pBkImg, cv.CV_BGR2GRAY)
        cv.CvtColor(pFrame, pFrImg, cv.CV_BGR2GRAY)

        cv.Convert(pFrImg,pBkMat)
        cv.Convert(pFrImg,pFrMat)
        cv.Convert(pFrImg,pFrameMat)
    else:
        cv.CvtColor(pFrame, pFrImg, cv.CV_BGR2GRAY)
        cv.Convert(pFrImg, pFrameMat)
        cv.Smooth(pFrameMat,pFrameMat,cv.CV_GAUSSIAN,3,0,0)
        cv.AbsDiff(pFrameMat,pBkMat,pFrMat)
        cv.Threshold(pFrMat, pFrImg, 60, 255.0, cv.CV_THRESH_BINARY)

        # cv.Erode(pFrImg,pFrImg,0,1)
        # cv.Dilate(pFrImg, pFrImg, 0, 1)

        cv.RunningAvg(pFrameMat,pBkMat,0.01,None)
        cv.Convert(pBkMat,pBkImg)

        cv.ShowImage("video", pFrame)
        cv.ShowImage("background", pBkImg)
        cv.ShowImage("foreground", pFrImg)

    if cv.WaitKey(1) & 0xFF == ord('q'):
        break
cv.DestroyAllWindows()


