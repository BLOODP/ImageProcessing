import cv2
import numpy as np

PSNR_B = 0
PSNR_G = 0
PSNR_R = 0
PSNR1 = 0

sumB = 0
sumG = 0
sumR = 0
mseB = 0
mseG = 0
mseR = 0

src = cv2.cv.LoadImage('/Users/heguangqin/Pictures/fengche.jpg',1)
cv2.cv.ShowImage('src',src)
print 'src : ',src.depth
yuv_image = cv2.cv.CreateImage(cv2.cv.GetSize(src),src.depth,3)
dst = cv2.cv.CreateImage(cv2.cv.GetSize(src),src.depth,3)
dst_yuv = cv2.cv.CreateImage(cv2.cv.GetSize(src),src.depth,3)

Y = cv2.cv.CreateImage(cv2.cv.GetSize(src),cv2.cv.IPL_DEPTH_8U,1)
U = cv2.cv.CreateImage(cv2.cv.GetSize(src),cv2.cv.IPL_DEPTH_8U,1)
V = cv2.cv.CreateImage(cv2.cv.GetSize(src),cv2.cv.IPL_DEPTH_8U,1)

# cv2.cv.ShowImage('Y',Y)

cv2.cv.CvtColor(src,yuv_image,cv2.cv.CV_BGR2YCrCb)
cv2.cv.ShowImage('yuv',yuv_image)
cv2.cv.Split(yuv_image,Y,U,V,None)
cv2.cv.ShowImage('Y',Y)
cv2.cv.ShowImage('u',U)
cv2.cv.ShowImage('V',V)

MatY = cv2.cv.CreateMat(Y.height,Y.width,cv2.cv.CV_64FC1)
MatU = cv2.cv.CreateMat(U.height,U.width,cv2.cv.CV_64FC1)
MatV = cv2.cv.CreateMat(V.height,V.width,cv2.cv.CV_64FC1)

DCTY = cv2.cv.CreateMat(Y.height,Y.width,cv2.cv.CV_64FC1)
DCTU = cv2.cv.CreateMat(U.height,U.width,cv2.cv.CV_64FC1)
DCTV = cv2.cv.CreateMat(V.height,V.width,cv2.cv.CV_64FC1)

cv2.cv.Scale(Y,MatY)
cv2.cv.Scale(U,MatU)
cv2.cv.Scale(V,MatV)

cv2.cv.DCT(MatY,DCTY,cv2.cv.CV_DXT_FORWARD)
cv2.cv.DCT(MatU,DCTU,cv2.cv.CV_DXT_FORWARD)
cv2.cv.DCT(MatV,DCTV,cv2.cv.CV_DXT_FORWARD)
print 'dcty',dir(DCTY)
print DCTY.rows,DCTY.cols,cv2.cv.Get2D(MatY,100,100),cv2.cv.Get2D(Y,100,100),cv2.cv.Get2D(DCTY,100,100)


for i in range(Y.height):
    for j in range(Y.width):
        valY = cv2.cv.Get2D(DCTY,i,j)
        valU = cv2.cv.Get2D(DCTU, i, j)
        valV = cv2.cv.Get2D(DCTV, i, j)
        if abs(valY[0]) < 10:
            cv2.cv.Set2D(DCTY,i,j,(0,))
        if abs(valU[0]) < 30:
            cv2.cv.Set2D(DCTU,i,j,(0,))
        if abs(valV[0]) < 5:
            cv2.cv.Set2D(DCTV,i,j,(0,))

arr = np.zeros((800, 1280), dtype='uint8')
for i in range(800):
    for j in range(1280):
        arr[i, j] = cv2.cv.Get2D(DCTV, i, j)[0]
# for i in range(U.height):
#     for j in range(U.width):
#         val = cv2.cv.Get2D(DCTU,i,j)
#         if abs(val[0]) < 800:
#             cv2.cv.Set2D(DCTU,i,j,(0,))
#
# for i in range(V.height):
#     for j in range(V.width):
#         val = cv2.cv.Get2D(DCTV,i,j)
#         if abs(val[0]) < 20:
#             cv2.cv.Set2D(DCTV,i,j,(0,))

cv2.cv.DCT(DCTY,MatY,cv2.cv.CV_DXT_INVERSE)
cv2.cv.DCT(DCTU,MatU,cv2.cv.CV_DXT_INVERSE)
cv2.cv.DCT(DCTV,MatV,cv2.cv.CV_DXT_INVERSE)

cv2.cv.Scale(MatY,Y)
cv2.cv.Scale(MatV,V)
cv2.cv.Scale(MatU,U)

cv2.cv.Merge(Y,U,V,None,dst_yuv)
cv2.cv.ShowImage('DCTed_Y',dst_yuv)

cv2.cv.CvtColor(dst_yuv,dst,cv2.cv.CV_YCrCb2BGR)
cv2.cv.ShowImage('dcted_src',dst)

for i in range(src.height):
    for j in range(src.width):
        srcVal = cv2.cv.Get2D(yuv_image,i,j)
        dstVal = cv2.cv.Get2D(dst_yuv,i,j)
        sumB += (srcVal[0] - dstVal[0]) * (srcVal[0] - dstVal[0])
        sumG += (srcVal[1] - dstVal[1]) * (srcVal[1] - dstVal[1])
        sumR += (srcVal[2] - dstVal[2]) * (srcVal[2] - dstVal[2])

mseB = sumB / (src.width * src.height)
mseG = sumG / (src.width * src.height)
mseR = sumR / (src.width * src.height)

PSNR_B = 10.0 * (np.log10(255.0 * 255.0 / mseB))
print 'pnsr b : ',PSNR_B
PSNR_G = 10.0 * (np.log10(255.0 * 255.0 / mseG))
print 'psnr g : ',PSNR_G
PSNR_R = 10.0 * (np.log10(255.0 * 255.0 / mseR))
print 'psnr r : ',PSNR_R
PSNR1 = (PSNR_B + PSNR_G + PSNR_G)/3
print 'psnr : ',PSNR1

cv2.cv.WaitKey(0)
cv2.cv.DestroyAllWindows()
print "--------------"

cv2.imshow('dcty',arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.warpPerspective()
