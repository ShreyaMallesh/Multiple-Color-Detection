#BGRtoHSV
import numpy as np
import cv2 as cv
img=cv.imread(r'F:\\puppies\\rgb.png')
hsvFrame = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsvFrame)
cv.imshow('image',img)
cv.waitKey(0)