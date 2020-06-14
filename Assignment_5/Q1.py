import cv2
import numpy as np

template=np.array([],dtype=np.uint8)
cap=cv2.VideoCapture(0)
pts=[]
count=0
def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pts
        global count
        global template
        if count<4:
            
            pts.append(y)
            count+=1
            pts.append(x)
            count+=1
            
            if count==4:
                template = cropped (cap.read() [1], pts)
            
    
def cropped(img,pts):
    cropped=frame[pts[1]:pts[3],pts[0]:pts[2]]
    return cropped

def comparison(img):
    global template
    greyimg= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    greytem=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

    res=cv2.matchTemplate(greyimg,greytem,cv2.TM_CCOEFF_NORMED)

    loc=np.where(res>=0.8)
    return loc

cv2.namedWindow ('webcam', cv2.WINDOW_NORMAL)
cv2.setMouseCallback ('webcam', mouse)

while True:
    x,frame=cap.read()
    if template.size > 3:
        h=template.shape[0]
        w=template.shape[1]
        loc= comparison(frame)

        for x, y in zip (*loc [::-1]):
                cv2.putText (frame, 'Object', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.rectangle (frame, (x, y), (x+w, y+h), (255, 255, 255), 1)
        cv2.imshow('object',template)

    cv2.imshow('webcam',frame)


    if cv2.waitKey (20) & 0xFF == ord('q'):
        break
