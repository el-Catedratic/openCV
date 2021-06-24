import cv2
import numpy as np

img = cv2.imread("resources/husky.jpg")

kernel = np.ones((5,5),np.uint8)

imgry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgry,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDialation,kernel,iterations = 1)

cv2.imshow("Husky",imgDialation)

cv2.waitKey(0)
