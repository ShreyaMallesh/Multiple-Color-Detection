import numpy as np
import cv2 as cv
img=cv.imread(r'F:\\puppies\\rgb.png')
hsvFrame = cv.cvtColor(img, cv.COLOR_BGR2HSV)
green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv.inRange(hsvFrame, green_lower, green_upper)
cv.imshow('bk',green_mask)
cv.imshow('image',img)
cv.waitKey(0)