import cv2

image = cv2.imread('resources/husky.jpg')

#Resized image
resized = cv2.resize(image,(500,500),interpolation=cv2.INTER_AREA)

cv2.imshow('Resized',resized)

#Graycolor

gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

#blurring
blur = cv2.GaussianBlur(resized,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Blurred",blur)

#edges
cvs = cv2.Canny(resized,125,175)
cv2.imshow("Canny",cvs)

#dilating
dil = cv2.dilate(resized,(3,3),iterations=3)
cv2.imshow("Dilated",dil) #the region with brighter pixels increases

#eroded
ero = cv2.erode(resized,(3,3),iterations=3) #the region having darker pixels increases
cv2.imshow("Eroded",ero)

cv2.waitKey(0)