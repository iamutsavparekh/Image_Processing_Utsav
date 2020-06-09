import cv2
import requests
import numpy as np

url = r"http://192.168.0.123:8080/shot.jpg"
counter=0
while True:
    counter+=1
    online_vid = requests.get(url)
    online_vid_arr = np.array(bytearray(online_vid.content),dtype = np.uint8)
    online_img = cv2.imdecode(online_vid_arr, -1)
    img = online_img
    rotated=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    flipped= cv2.flip(rotated,-1) # 1
    if counter%2==0:
        cv2.imshow('Img',rotated)
    else:
        cv2.imshow('Img',flipped)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cv2.destroyAllWindows()
