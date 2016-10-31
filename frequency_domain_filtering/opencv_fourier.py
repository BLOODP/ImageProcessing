import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
print type(magnitude_spectrum)
print magnitude_spectrum.dtype
print magnitude_spectrum.shape

print magnitude_spectrum[100:110,100:120]

m = np.around(magnitude_spectrum)
print m.dtype
print m[100:110,100:120]

m8 = np.array(m.tolist(),dtype='uint8')

print m8.dtype
print m8[100:110,100:120]

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
print 'img_back dtype : ',img_back.dtype
print img_back[100:110,100:110]

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

print 'img_back dtype : ',img_back.dtype
print img_back[100:110,100:110]
scale = 255/(img_back.max()-img_back.min())
back = (img_back-img_back.min())*scale

print back[100:110,100:110]
back = np.array(np.around(back).tolist(),dtype='uint8')


cv2.imshow('src',img)
cv2.imshow('magnitude_spectrum',m8)
cv2.imshow('back',back)

cv2.waitKey(0)
cv2.destroyAllWindows()