import cv2

img= cv2.imread('E:/Robocon Internship/Git/Robocon_Internship/Assignment_2/bgimg.jpg')
print(img.shape)
cv2.line(img,(0,0),(956,1300),(255,0,0),3)
cv2.imshow('Image',img)
cv2.waitKey(0)
