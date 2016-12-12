import cv2.cv as cv
import cv2
import numpy

capture = cv.CaptureFromFile('/Users/heguangqin/Downloads/yilake.mp4')
nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))

motion = None
previousImage = None

pause = False
if capture:

    cv.NamedWindow('motion',1)
    for i in range(100):
        if not cv.GrabFrame(capture):
            break

        image = cv.RetrieveFrame(capture)
        if image:
            if not motion:
                print 'not motion...........'
                previousImage = cv.CreateImage((image.width, image.height),image.depth,image.channels)
                cv.Copy(image,previousImage)
                motion = cv.CreateImage((image.width, image.height),8,1)
                cv.Zero(motion)
                motion.origin = image.origin
        cv.Copy(image, previousImage)

        print 'i;: ',i
        cv.ShowImage('motion',previousImage)
        if cv.WaitKey(1) & 0xFF == ord('q'):
            break
cv.DestroyAllWindows()

