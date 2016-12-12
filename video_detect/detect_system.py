import cv2
import cv2.cv as cv

capture = cv.CaptureFromFile('/Users/heguangqin/Downloads/yilake.mp4')
nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))

print 'frames: ',nbFrames
frameImg = cv.QueryFrame(capture)
for i in xrange(100):
    frameImg = cv.QueryFrame(capture)
    filename = '/workplace/images/yilake_image_%d.jpg' %i
    cv.SaveImage(filename,frameImg)
    print filename
    cv.ShowImage("The Video", frameImg)
    if cv.WaitKey(1) & 0xFF == ord('q'):
        break
cv.DestroyAllWindows()