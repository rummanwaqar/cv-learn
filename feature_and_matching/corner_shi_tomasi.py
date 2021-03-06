import numpy as np 
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# shi-tomasi detector
# params: int8 gray image, no.of corners, ...
# 		  quality between 0-1 (minimum quality of corner below which it is rejected), ...
#		  minimum euclidean distance between points

corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
corners = np.int0(corners) # convert to int

for i in corners:
	x,y = i.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)

plt.imshow(img), plt.show()	