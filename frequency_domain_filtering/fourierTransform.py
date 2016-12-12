# coding=utf-8
import numpy as np
import cv2

img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg', 0)
img = cv2.resize(img, (800, 600))

cv2.imshow('img', img)

#  numpy实现傅立叶变换
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#   显示频率图谱
magnitude_spectrum = 20 * np.log(np.abs(fshift))
magnitude_spectrum = np.array(np.around(magnitude_spectrum).tolist(), dtype='uint8')
cv2.imshow('magnitude_spectrum', magnitude_spectrum)

#     numpy实现傅立叶逆变换
rows, cols = img.shape
crow, ccol = rows / 2, cols / 2

#     去除高频成分
fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
img_back = np.array(np.around(img_back).tolist(), dtype='uint8')
cv2.imshow('back_without_high_fq', img_back)

#       opencv实现傅立叶变换
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

#       显示频率图谱
magnitude_spectrum1 = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
magnitude_spectrum1 = np.array(np.around(magnitude_spectrum1).tolist(), dtype='uint8')
cv2.imshow('magnitude_spectrum1', magnitude_spectrum1)

#       去除高频成分
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

#      opencv实现逆变换
dfshift = dft_shift * mask
df_ishift = np.fft.ifftshift(dfshift)
dimg_back = cv2.idft(df_ishift)
dimg_back = cv2.magnitude(dimg_back[:, :, 0], dimg_back[:, :, 1])
scale = 255 / (dimg_back.max() - dimg_back.min())
back = (dimg_back - dimg_back.min()) * scale
back = np.array(np.around(back).tolist(), dtype='uint8')
cv2.imshow("dimg_back", back)

cv2.waitKey(0)
cv2.destroyAllWindows()
