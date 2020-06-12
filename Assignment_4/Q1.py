import cv2
import requests

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(img[y,x])
while True:
    cap=cv2.VideoCapture(0)
    ret,img = cap.read()
    print(img.size)
    print(img.shape)
    cv2.namedWindow('img')
    cv2.setMouseCallback('img',mouse)
    cv2.imshow('img',img)
    key= cv2.waitKey(1) 
    if key == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
   