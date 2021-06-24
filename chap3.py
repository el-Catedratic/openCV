#REsizing images
import cv2
import numpy as np

img = cv2.imread("resources/husky.jpg")

print(img.shape)

imgRes = cv2.resize(img,(1024,1024))

imgCrop = img[640:1024,640:1024]

cv2.imshow("Husky ",imgCrop)

cv2.waitKey(10000)