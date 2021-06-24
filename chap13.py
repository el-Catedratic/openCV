import cv2
import numpy as np

#Bitwise Ops
blank = np.zeros((500,500),dtype=np.uint8)

rec = cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cir = cv2.circle(blank.copy(),(200,200),200,255,-1)

bit_and = cv2.bitwise_and(rec,cir)
cv2.imshow("and",bit_and)

#similarly for or,xor


