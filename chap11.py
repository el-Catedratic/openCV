#color channel

import cv2
import numpy as np

img = cv2.imread("resources/husky.jpg")
resize = cv2.resize(img,(500,500))
cv2.imshow("Resize",resize)

b,g,r = cv2.split(resize)

cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)

merge = cv2.merge([b,g,r])
cv2.imshow("merge",merge)

blank = np.zeros(resize.shape[:2],np.uint8)

blue = cv2.merge([b,blank,blank])
cv2.imshow("Bluish",blue)

cv2.waitKey(0)