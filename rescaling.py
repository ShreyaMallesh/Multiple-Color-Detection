import cv2 as cv

def rescaleFrame(img,scale=0.75):
    width= int(img.shape[1] * scale)
    height= int(img.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img= cv.imread("F:\\puppies\\poo.jpeg")

img_resized=rescaleFrame(img)
cv.imshow("Dog",img_resized)
cv.imshow("Pup",img)

cv.waitKey(0)
  