#bluecontouring
import numpy as np
import cv2 as cv
img=cv.imread(r'F:\\puppies\\aqua.png')
hsvFrame = cv.cvtColor(img, cv.COLOR_BGR2HSV)
kernal = np.ones((5, 5), "uint8")
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv.inRange(hsvFrame, blue_lower, blue_upper)
#blue_mask = cv.dilate(blue_mask, kernal)
res_blue = cv.bitwise_and(img, img,
								mask = blue_mask)
contours, hierarchy = cv.findContours(blue_mask,
									cv.RETR_TREE,
									cv.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	area = cv.contourArea(contour)
	if(area > 300):
		x, y, w, h = cv.boundingRect(contour)
		imageFrame = cv.rectangle(img, (x, y),
								(x + w, y + h),
								(255, 0, 0), 2)
			
		cv.putText(imageFrame, "Blue Colour", (x, y),
					cv.FONT_HERSHEY_SIMPLEX,
					1.0, (255, 0, 0))
cv.imshow('image',img)
cv.waitKey(0)