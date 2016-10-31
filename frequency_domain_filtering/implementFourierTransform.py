import numpy as np
import cv2

src = cv2.cv.LoadImage("/Users/heguangqin/Pictures/source_1.jpg", 0)
print "src channels", src.channels
cv2.cv.NamedWindow("src", 0)
cv2.cv.ShowImage("src", src)

Fourier = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 2)
dst = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 2)
ImageRe = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 1)
ImageIm = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 1)
Image = cv2.cv.CreateImage(cv2.cv.GetSize(src), src.depth, src.channels)
ImageDst = cv2.cv.CreateImage(cv2.cv.GetSize(src), src.depth, src.channels)


def fft2(src, dst):
    image_Re = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 1)
    image_Im = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 1)
    Fourier = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 2)
    cv2.cv.ConvertScale(src, image_Re, 1, 0)
    cv2.cv.Zero(image_Im)
    cv2.cv.Merge(image_Re, image_Im, None, None, Fourier)
    cv2.cv.DFT(Fourier, dst, cv2.cv.CV_DXT_FORWARD)


def fft2shift(src, dst):
    image_Re = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 1)
    image_Im = cv2.cv.CreateImage(cv2.cv.GetSize(src), cv2.cv.IPL_DEPTH_64F, 1)
    cv2.cv.Split(src, image_Re, image_Im, None, None)
    cv2.cv.Pow(image_Re, image_Re, 2)
    cv2.cv.Pow(image_Im, image_Im, 2)
    cv2.cv.Add(image_Re, image_Im, image_Re)
    cv2.cv.Pow(image_Re, image_Re, 0.5)
    cv2.cv.AddS(image_Re, cv2.cv.Scalar(1.0), image_Re)
    cv2.cv.Log(image_Re, image_Re)

    nRow = src.height
    nCol = src.width
    cy = nRow / 2
    cx = nCol / 2
    minValue = 1000
    maxValue = 0
    for j in range(cy):
        for i in range(cx):
            tmp13 = cv2.cv.Get2D(image_Re, j, i)
            if minValue >= tmp13[0]: minValue = tmp13[0]
            if maxValue <= tmp13[0]: maxValue = tmp13[0]

            cv2.cv.Set2D(image_Re, j, i, cv2.cv.Get2D(image_Re, j + cy, i + cx))
            cv2.cv.Set2D(image_Re, j + cy, i + cx, tmp13)
            tmp24 = cv2.cv.Get2D(image_Re, j, i + cx)
            cv2.cv.Set2D(image_Re, j, i + cx, cv2.cv.Get2D(image_Re, j + cy, i))
            cv2.cv.Set2D(image_Re, j + cy, i, tmp24)

    # mask = [0,0]
    # cv2.cv.MinMaxLoc(image_Re,mask)
    print 'mask:', minValue, maxValue
    scale = 255 / (maxValue - minValue)
    shift = -minValue * scale
    cv2.cv.ConvertScale(image_Re, dst, scale, shift)


fft2(src, Fourier)
fft2shift(Fourier, Image)
cv2.cv.DFT(Fourier, dst, cv2.cv.CV_DXT_INV_SCALE)
cv2.cv.Split(dst, ImageRe, ImageIm, None, None)
cv2.cv.Pow(ImageRe, ImageRe, 2)
cv2.cv.Pow(ImageIm, ImageIm, 2)
cv2.cv.Add(ImageRe, ImageIm, ImageRe)
cv2.cv.Pow(ImageRe, ImageRe, 0.5)

minVal = 10000
maxVal = -1

for k in range(ImageRe.height):
    for w in range(ImageRe.width):
        sc = cv2.cv.Get2D(ImageRe, k, w)[0]
        if minVal > sc: minVal = sc
        if maxVal < sc: maxVal = sc
print 'minVal,maxVal :', minVal, maxVal
scale = 255 / (maxVal - minVal)
shift = -minVal * scale
cv2.cv.ConvertScale(ImageRe, ImageDst, scale, shift)

cv2.cv.ShowImage('sdt', Image)
cv2.cv.ShowImage('dst', ImageDst)
cv2.cv.WaitKey(0)
cv2.cv.DestroyAllWindows()
