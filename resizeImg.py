import cv2

img = cv2.imread("/Users/heguangqin/Downloads/logo.PNG");
# img = img[]
cv2.imshow("image",img);
print img.shape
cv2.waitKey(0)
cv2.destroyAllWindows();