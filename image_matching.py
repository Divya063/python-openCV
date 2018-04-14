import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('feature-match.jpg',0)
img2 = cv2.imread('feature-match1.jpg',0)

ret1, diff1 = orb.detectAndCompute(img1,None)
ret2, diff2 = orb.detectAndCompute(img2,None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = matcher.match(diff1,diff2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,ret1,img2,ret2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()