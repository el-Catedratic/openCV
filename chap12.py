import cv2

img = cv2.imread("resources/husky.jpg")

resize = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow("Og",resize)

#Gaussian Blurr
gau = cv2.GaussianBlur(resize,(5,5),0) #3rd param std deviation in x dir
cv2.imshow("Gaussian",gau)

#median blur
med = cv2.medianBlur(resize,5)
cv2.imshow("Median",med)

bil = cv2.bilateralFilter(resize,5,15,15)
cv2.imshow("Bilateral ",bil)

cv2.waitKey(0)