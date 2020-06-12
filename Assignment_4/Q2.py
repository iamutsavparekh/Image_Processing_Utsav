import cv2
import numpy as np
import requests
arr=[]

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        arr.append(x)
        arr.append(y)

while True:
    img= cv2.imread('E:/Robocon Internship/Git/Robocon_Internship/Assignment_4/bgimg.jpg')
    cv2.namedWindow("Img")
    ref1= cv2.setMouseCallback("Img",mouse)
    cv2.imshow("Img",img)
    if len(arr)==4:
        cropped=img[arr[1]:arr[3],arr[0]:arr[2]]
        cv2.imshow("Cropped",cropped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cv2.destroyAllWindows()