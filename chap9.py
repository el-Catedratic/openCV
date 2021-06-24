#Contour Detection

import cv2
import numpy as np

img = cv2.imread("resources/husky.jpg")
resize = cv2.resize(img,(500,500),interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
blank = np.zeros(resize.shape,np.uint8)

cv2.imshow("Og",resize)

canny = cv2.Canny(resize,125,255)
cv2.imshow("canny",canny)

contours,hierarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))

ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow("Thresholded",thresh)

#contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#print(len(contours))

cv2.drawContours(blank,contours,-1,(0,0,255),2)
cv2.imshow("Contours",blank)

cv2.waitKey(0)
