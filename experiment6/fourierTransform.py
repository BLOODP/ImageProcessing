import numpy as np
import cv2

img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg',0)
cv2.imshow('img',img)
f = np.fft.fft2(img)
print 'f dtype',f.dtype
fshift = np.fft.fftshift(f)
print 'fshift dtype',fshift.dtype
magnitude_spectrum = 20*np.log(np.abs(fshift))
magnitude_spectrum = np.array(np.around(magnitude_spectrum).tolist(),dtype='uint8')
cv2.imshow('magnitude_spectrum',magnitude_spectrum)

rows, cols = img.shape
crow,ccol = rows/2 , cols/2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
print img_back.dtype
img_back = np.abs(img_back)
print img_back.dtype
print img_back[100:110,100:110]
img_back = np.array(np.around(img_back).tolist(),dtype='uint8')
cv2.imshow('back',img_back)



dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum1 = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
magnitude_spectrum1 = np.array(np.around(magnitude_spectrum1).tolist(),dtype='uint8')
cv2.imshow('magnitude_spectrum1',magnitude_spectrum1)

mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

dfshift = dft_shift*mask
df_ishift = np.fft.ifftshift(dfshift)
dimg_back = cv2.idft(df_ishift)
print dimg_back.shape
dimg_back = cv2.magnitude(dimg_back[:,:,0],dimg_back[:,:,1])
print dimg_back.dtype
scale = 255/(dimg_back.max()-dimg_back.min())
back = (dimg_back-dimg_back.min())*scale
back = np.array(np.around(back).tolist(),dtype='uint8')
cv2.imshow("dimg_back",back)

cv2.waitKey(0)
cv2.destroyAllWindows()