import cv2
import numpy as np

img = cv2.imread("resources/husky.jpg")

#resizing with differnet interpolations

resized = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
resized_area = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
resized_linear = cv2.resize(img,(500,500),interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized",resized)
cv2.imshow("Og",resized_area)
cv2.imshow("Linear",resized_linear)


def transform(x,y):
    trans_mat = np.float64([[1,0,x],[0,1,y]])
    dimensions = (resized.shape[0],resized.shape[1])
    return cv2.warpAffine(resized,trans_mat,dimensions)

trans_img = transform(-45,-50) #-x for left,-y for up 
cv2.imshow("Transform image",trans_img)   

#print(len(resized.shape))

#rotation
def rotate(img,angle,rtpt = None):
    (height,width) = resized.shape[:2]

    if rtpt is None:
        rtpt = (width//2,height//2)

    rotmat = cv2.getRotationMatrix2D(rtpt,angle,1.0)
    dimensions = (width,height)
    return cv2.warpAffine(img,rotmat,dimensions)

rot_img = rotate(resized,45)
cv2.imshow("Rotate",rot_img)        

#flipping
flip = cv2.flip(resized,-1)
cv2.imshow("Flipped",flip)


cv2.waitKey(0)