import numpy as np 
import cv2

img= cv2.imread("scene.jpg",cv2.IMREAD_COLOR)

img[100:150, 100:150]=[255, 255, 255]

sun=img[37:111,107:194]
img[0:74, 0:87]=sun



cv2.imshow("scene", img)
cv2.waitKey(0)
cv2.destroyAllWindows()