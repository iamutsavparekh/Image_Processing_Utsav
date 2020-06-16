import cv2
import numpy as np

while True:
    img=cv2.imread('E:/Robocon Internship/Git/Robocon_Internship/Assignment_6/img.jpg')
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((5,5))
    close=cv2.morphologyEx(img_gray,cv2.MORPH_CLOSE,kernel)
    canny = cv2.Canny (close, 50, 225)

    cv2.imshow('img',img)
    cv2.imshow('edge',canny)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()