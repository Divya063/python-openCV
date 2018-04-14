import numpy as np
import cv2

img= cv2.imread('lowlight_bookpage.jpg')
return_val, threshold = cv2.threshold(img, 9, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imwrite('clear_image.jpg', gaus)


cv2.imshow('Adaptive threshold',gaus)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()