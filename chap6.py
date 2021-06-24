#Drawing on images
import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype = np.uint8)

cv2.imshow("Blank_og",blank)

#coloring image

blank[:]  = (255,0,0)
cv2.imshow('Red',blank)



#Drawing a rectangle

cv2.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness = -1)
cv2.imshow('Rect',blank)

cv2.rectangle(blank,(blank.shape[0]//2,blank.shape[1]//2),(500,500),(255,255,255),thickness = -1)
cv2.imshow('Rect',blank)
# Drawing a circle

cv2.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),(100),(0,0,0),thickness = 10)
cv2.imshow("Circle",blank)

# Adding Text

cv2.putText(blank,'Hey this is Akhil',(0,255),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
cv2.imshow("Text Added",blank)


cv2.waitKey(0)