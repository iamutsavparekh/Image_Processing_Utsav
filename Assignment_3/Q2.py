import cv2
import numpy as np
import time

img= cv2.imread('E:/Robocon Internship/Git/Robocon_Internship/Assignment_2/bgimg.jpg')
h,w,c=img.shape
htdiff=int(h/7)
wtdiff=int(w/7)
htb=0
hta=htdiff
counter=0
while True:
    while hta<=h:
        if counter%2==0:
            wtb=0
            wta=wtdiff
            while wta<=w: 
                img[htb:hta,wtb:wta]=np.random.randint(0,255,(3))
                cv2.imshow('Img',img)
                time.sleep(0.5)
                wtb+=wtdiff
                wta+=wtdiff
        else:
            wtb=w-wtdiff
            wta=w
            while wtb>=0: 
                img[htb:hta,wtb:wta]=np.random.randint(0,255,(3))
                cv2.imshow('Img',img)
                time.sleep(0.5)
                wtb-=wtdiff
                wta-=wtdiff
        htb+=htdiff
        hta+=htdiff
        counter+=1
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break;
cv2.destroyAllWindows()