#Advanced Module
#color spaces

import cv2

img = cv2.imread("resources/husky.jpg")
resize = cv2.resize(img,(500,500))
cv2.imshow("Resize",resize)

gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

#BGR to HSV
hsv = cv2.cvtColor(resize,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)

#BGR to LAB
lab = cv2.cvtColor(resize,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",lab)

rgb = cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",rgb)

hsv = cv2.cvtColor(rgb,cv2.COLOR_BGR2HSV)
cv2.imshow("HSVRGB",hsv)

cv2.waitKey(0)
