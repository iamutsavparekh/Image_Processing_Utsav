import cv2
import numpy as np



frame=cv2.imread('E:/Robocon Internship/Git/Robocon_Internship/Assignment_7/img.jpg')
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.namedWindow('Transformed',cv2.WINDOW_NORMAL)
lower_bound=np.array([5,0,109])
upper_bound=np.array([85,46,245])

maskfinal= cv2.inRange(hsv,lower_bound,upper_bound)

res=cv2.bitwise_and(frame,frame,mask=maskfinal)

contours_found,hierarchy=cv2.findContours(maskfinal,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

areas=[cv2.contourArea(c) for c in contours_found]

max_index=np.argmax(areas)

max_contour=contours_found[max_index]

x,y,w,h=cv2.boundingRect(max_contour)

perimeter=cv2.arcLength(max_contour,True)

ROI=cv2.approxPolyDP(max_contour,0.01*perimeter,True)

arr1=np.array([ROI[1],ROI[0],ROI[2],ROI[3]],np.float32)
arr2=np.array([(0,0),(1000,0),(0,1000),(1000,1000)],np.float32)

perspective = cv2.getPerspectiveTransform(arr1,arr2)
transformed = cv2.warpPerspective(frame,perspective,(1000,1000))

cv2.drawContours(frame,[ROI],-1,(255,0,0),15)

cv2.imshow('frame',frame)
cv2.imshow("Transformed",transformed)
cv2.waitKey(0)