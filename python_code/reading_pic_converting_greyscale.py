import cv2 as cv
import numpy as np

img = cv.imread('F:\image_processing\images\id.jpg' ,-1)
img1 = cv.imread('F:\image_processing\images\id.jpg',0)
cv.imwrite('F:\image_processing\images\greyscale.jpg',img1)
cv.imshow('image1',img1)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
