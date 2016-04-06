import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image
filename = 'chessboard.png'
img = cv2.imread(filename)
# convert to float32 grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# harris detector 
# params: img, blocksize, ksize, k
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
#plt.imshow(dst, interpolation='nearest', cmap='gray')
#plt.colorbar()
#plt.show()
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('Corners', img)
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()