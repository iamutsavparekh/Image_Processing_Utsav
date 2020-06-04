import numpy as np
import cv2
import requests

url = r"http://192.168.0.123:8080/shot.jpg"
counter=0
while True:
    counter +=1
    n=int(input())
    online_vid = requests.get(url)
    online_vid_arr = np.array(bytearray(online_vid.content),dtype = np.uint8)
    online_img = cv2.imdecode(online_vid_arr, -1)
    img = online_img
    flipped= cv2.flip(img,-1) 
    
    if counter<=n:
        cv2.imshow('image_window',img)

    cv2.imshow('image_window',flipped)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
cv2.destroyAllWindows()
