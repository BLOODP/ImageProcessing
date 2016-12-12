import cv2
import numpy as np

cap = cv2.VideoCapture('/Users/heguangqin/Downloads/yilake.mp4')
nFrames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

print 'nFrames : ', nFrames

pause = False
previousImage = None
motion = None
inited = False

if cap.isOpened():
    while not pause:
        ret,image = cap.read()
        if not inited:
            motion = np.zeros((image.shape[0],image.shape[1]),dtype='uint8')
            previousImage = np.zeros_like(image)
            inited = True

        image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        previousImage_gray = cv2.cvtColor(previousImage,cv2.COLOR_BGR2GRAY)
        motion = np.array(image_gray.tolist(),dtype='int32') - np.array(previousImage_gray.tolist(),dtype='int32')
        motion = np.absolute(motion)
        motion = np.array(motion.tolist(),dtype='uint8')
        print motion.shape

        cv2.imshow('frame',motion)
        previousImage = image.copy()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()