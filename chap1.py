import cv2


''' print("Loading Image ")

img = cv2.imread("resources/husky.jpg")

cv2.imshow("Output",img)
cv2.waitKey(0)'''

print("Loading Video")
''' for videocapture the parameter maybe a file path to specific video or  the camera id'''
vid = cv2.VideoCapture(0) 
vid.set(3,640)
vid.set(4,480)
vid.set(10,70)

while True:
    success,vi = vid.read()
    cv2.imshow("Video",vi)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    