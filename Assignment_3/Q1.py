import cv2
import numpy as np
import time

img= cv2.imread('E:/Robocon Internship/Git/Robocon_Internship/Assignment_2/bgimg.jpg')
h,w,c=img.shape
htdiff=int(h/7)
wtdiff=int(w/7)
wtb=0
wta=wtdiff
htb=0
hta=htdiff
while True:
    while hta<=h:
        while wta<=w: 
            cv2.imshow('Img',img)
            randno=np.random.randint(0,255,(3))
            img[htb:hta,wtb:wta]=randno
            wtb+=wtdiff
            wta+=wtdiff
        wtb=0
        wta=wtdiff
        htb+=htdiff
        hta+=htdiff
        
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break;
cv2.destroyAllWindows()