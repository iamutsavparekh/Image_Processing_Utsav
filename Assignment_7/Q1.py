import cv2
import requests
import numpy as np

def nothing(x):
    print(x)
cap=cv2.VideoCapture(0)
cv2.namedWindow('colorpalette')

cv2.createTrackbar('Lower_H','colorpalette',0,180,nothing)
cv2.createTrackbar('Higher_H','colorpalette',0,180,nothing)

cv2.createTrackbar('Lower_S','colorpalette',0,100,nothing)
cv2.createTrackbar('Higher_S','colorpalette',0,100,nothing)

cv2.createTrackbar('Lower_V','colorpalette',0,100,nothing)
cv2.createTrackbar('Higher_V','colorpalette',0,100,nothing)

while True:
    cv2.namedWindow('img')
    ret,img=cap.read()

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    high_h=cv2.getTrackbarPos('Higher_H','colorpalette')
    low_h=cv2.getTrackbarPos('Lower_H','colorpalette')
    high_s=cv2.getTrackbarPos('Higher_S','colorpalette')
    low_s=cv2.getTrackbarPos('Lower_S','colorpalette')
    high_v=cv2.getTrackbarPos('Higher_V','colorpalette')
    low_v=cv2.getTrackbarPos('Lower_V','colorpalette')

    higher_c=np.array([high_h,high_s,high_v])
    lower_c=np.array([low_h,low_s,low_v])

    print(higher_c)
    print(lower_c)    
    mask=cv2.inRange(hsv,lower_c,higher_c)
    mask=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow('img',img)
    cv2.imshow('Masked',mask)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows