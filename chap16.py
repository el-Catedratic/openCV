#adaptive thresholding

import cv2

img = cv2.imread("resources/husky.jpg")
resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)

thresh,thresholded = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow("Thresholded",thresholded)

cv2.waitKey(0)