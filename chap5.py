#RESCALING LIVE VIDEo
import cv2

capture = cv2.VideoCapture(0)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue,frame = capture.read()
    #changeRes(20,30)
    cv2.imshow('LiveVideo',frame)
    #frame_res = changeRes(200,300)
    #cv2.imshow('Shortsized',frame_res)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break