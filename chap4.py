#Rescaling Videos & images
import cv2

def Rescale(frame,scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture('resources/vid1.webm')

while True:
    isTrue,frame = capture.read()
    cv2.imshow('Video_og',frame)
    frame_reized = Rescale(frame,0.7)
    cv2.imshow('Video_res',frame_reized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break;

capture.release()        
cv2.destroyAllWindows()

