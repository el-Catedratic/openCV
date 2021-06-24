#masking
import cv2
import numpy as np

img = cv2.imread("resources/husky.jpg")

resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)

blank = np.zeros(resize.shape[:2],dtype=np.uint8)

mask = cv2.circle(blank,(200,200),200,255,-1)

msk = cv2.bitwise_and(resize,resize,mask=mask)
cv2.imshow("MASKED",msk)

cv2.waitKey(0)

