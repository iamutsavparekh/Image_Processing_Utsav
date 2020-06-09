import cv2
import requests
import numpy as np
import time

url = r"http://192.168.9.31:8080/shot.jpg"
start=time.time()
while True:
    online_vid = requests.get(url)
    online_vid_arr = np.array(bytearray(online_vid.content),dtype = np.uint8)
    online_img = cv2.imdecode(online_vid_arr, -1)
    img = online_img 
    flipped= cv2.flip(img,-1) 
    endtime=time.time()
    diff=int(endtime-start)
    print(diff)
    if diff % 5 == 0:
        cv2.imshow('image_window',flipped)
    else:
        cv2.imshow('image_window',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cv2.destroyAllWindows()
