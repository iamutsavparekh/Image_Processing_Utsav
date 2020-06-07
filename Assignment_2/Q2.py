import cv2
import numpy as np
import requests

url = r"http://192.168.9.31:8080/shot.jpg"
counter=0
while True:
    counter+=1
    online_vid = requests.get(url)
    online_vid_arr = np.array(bytearray(online_vid.content),dtype = np.uint8)
    online_img = cv2.imdecode(online_vid_arr, -1)
    img = online_img
    cv2.imwrite('Image_%s.jpg' %counter ,img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break;
cv2.destroyAllWindows()
   