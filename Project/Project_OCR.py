import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import tkinter as tk
from tkinter import filedialog,Text
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox

root= tk.Tk()
root.title("Welcome to OCR Application")
arr=[]
texts=''
canvas=tk.Canvas(root, height=650, width=800, bg='light blue')
frame=tk.Frame(canvas,bg='white')
frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

original_img=np.zeros((),np.uint8)
gaussianblur=np.zeros((),np.uint8)
sharpened=np.zeros((),np.uint8)
img1=np.zeros((),np.uint8)
transformed=np.zeros((),np.uint8)
cropped=np.zeros((),np.uint8)

#functions
def import_btn_clicked():
    global original_img
    filename=filedialog.askopenfilename(initialdir='E:\Robocon Internship\Git\Robocon_Internship\Project',title='Select an Image',filetypes=(('JPG','*.jpg'),('PNG','*.png'),('All Files','*.*')))
    original_img=cv2.imread(filename)
    cv2.imshow('img',original_img)
    cv2.waitKey(0)
        
def ocr_btn_clicked():
    global texts
    global img1
    img1=np.copy(original_img)
    str1=''
    data=pytesseract.image_to_data(img1,output_type=Output.DICT)
    no_word=len(data['text'])
    for i in range(no_word):
        if int(data['conf'][i])>50:
            x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
            str1=str1+data['text'][i]+' '
            cv2.imshow('img',img1)
            cv2.waitKey(100)
    texts=str1

def savetext_btn_clicked():
    f=open("OCR_Text.txt","w+")
    f.write(texts)
    f.close()

def show_btn_clicked(): 
    textbox=tk.Frame(frame)
    text1=Text(textbox, fg='black', bg='#fcffc2', wrap=WORD)
    text1.pack()
    textbox.place(relx=0.25,rely=0.3,relwidth=0.47,relheight=0.55)          
    save_text=tk.Button(frame,text='Save as Text', fg='blue', padx=1, pady=1, command=savetext_btn_clicked)
    save_text.pack()
    save_text.place(relx=0.8,rely=0.3)
    text1.insert('1.0',texts)

def og_btn_clicked():
    og_img=np.copy(original_img)
    cv2.imshow('og_img',og_img)

def autocrop_btn_clicked():
    global transformed
    img= np.copy(original_img)
    ratio = img.shape[1]/img.shape[0]
    height = int(1100/ratio)
    TransformedImage = cv2.resize(img,(1100,height))

    img_gray = cv2.cvtColor(TransformedImage,cv2.COLOR_BGR2GRAY)
    adaptive = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,55,3)
    canny = cv2.Canny(adaptive,150,250)

    contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    area = [cv2.contourArea(x) for x in contours]
    max_index = np.argmax(area)
    max_contour = contours[max_index]
    perimeter = cv2.arcLength(max_contour,True)
    region = cv2.approxPolyDP(max_contour,0.01*perimeter,True)


    if len(region) == 4:

        cv2.drawContours(TransformedImage,[region],-1,(255,0,0),10)
        lst = [region[0],region[3],region[1],region[2]]
        pt1 = np.array(lst,np.float32)
        pt2 = np.array([(0, 0), (600, 0), (0, 600), (600, 600)],np.float32)

        perspective = cv2.getPerspectiveTransform(pt1,pt2)
        transformed = cv2.warpPerspective(TransformedImage, perspective, (600,600))    

        cv2.imshow('Warped Image',transformed)
        cv2.waitKey(0)

def mouse(event,x,y,flags,param):
    global arr
    if event == cv2.EVENT_LBUTTONDOWN:
        arr.append(x)
        arr.append(y)

def manual_crop_clicked():
    global cropped
    while True:
        img=np.copy(original_img)
        cv2.namedWindow("Img")
        cv2.setMouseCallback("Img",mouse)
        cv2.imshow("Img",img)
        if len(arr)==4:
            cropped=img[arr[1]:arr[3],arr[0]:arr[2]]
            cv2.imshow("Cropped",cropped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def blur_btn_clicked():
    global gaussianblur
    img=np.copy(original_img)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussianblur=cv2.GaussianBlur(img,(25,25),2)
    cv2.imshow('Gaussian Blur',gaussianblur) 

def sharpen_btn_clicked():
    global sharpened
    img=np.copy(original_img)
    kernel=np.array([-1,-1,-1,
                    -1,9,-1,
                    -1,-1,-1 ])
    sharpened= cv2.filter2D(img,-1,kernel)
    cv2.imshow("Sharpened",sharpened)
    cv2.waitKey(0)

def save_image_clicked():
    counter=0
    if np.any(img1):
        cv2.imwrite('OCR.jpg',img1)  
        counter+=1
    if np.any(transformed):
        cv2.imwrite('Auto_Cropped.jpg',transformed)
        counter+=1
    if np.any(cropped):
        cv2.imwrite('Manual_Cropped.jpg',cropped)
        counter+=1 
    if np.any(gaussianblur):
        cv2.imwrite('Blurred.jpg',gaussianblur)  
        counter+=1
    if np.any(sharpened):
        cv2.imwrite('Sharpened.jpg',sharpened)  
        counter+=1
    if counter!=0:
        messagebox.showinfo('Notification','Image saved')
    else:
        messagebox.showinfo('Notification','No content to save')

def exit_btn_clicked():
    cv2.destroyAllWindows()
    exit()

import_btn=tk.Button(frame,text='Import',fg='blue', padx=3, pady=2, command=import_btn_clicked)
import_btn.pack()
import_btn.place(relx=0.025,rely=0.05)

ocr_btn=tk.Button(frame,text='OCR',fg='blue', padx=3, pady=2, command=ocr_btn_clicked)
ocr_btn.pack()
ocr_btn.place(relx=0.025,rely=0.15)

text_btn=tk.Button(frame,text='Show Text',fg='blue', padx=3, pady=2, command=show_btn_clicked)
text_btn.pack()
text_btn.place(relx=0.025,rely=0.25)

og_img_btn=tk.Button(frame,text='Show Original Image',fg='blue', padx=3, pady=2, command=og_btn_clicked)
og_img_btn.pack()
og_img_btn.place(relx=0.025,rely=0.35)

w=tk.Label(frame, text='Text will be displayed here', fg='#09b022',padx=3)
w.pack()
w.place(relx=0.25, rely=0.20)

auto_crop=tk.Button(frame,text='Auto Crop', fg='blue', padx=1, pady=1, command=autocrop_btn_clicked)
auto_crop.pack()
auto_crop.place(relx=0.025,rely=0.45)

manual_crop=tk.Button(frame,text='Manual Crop', fg='blue', padx=1, pady=1, command=manual_crop_clicked)
manual_crop.pack()
manual_crop.place(relx=0.025,rely=0.55)

blur_button=tk.Button(frame,text='Blur', fg='Blue', padx=1, pady=1, command=blur_btn_clicked)
blur_button.pack()
blur_button.place(relx=0.025,rely=0.65)

sharpen_button=tk.Button(frame,text='Sharpen', fg='Blue', padx=1, pady=1, command=sharpen_btn_clicked)
sharpen_button.pack()
sharpen_button.place(relx=0.025,rely=0.75)

save_button=tk.Button(frame,text='Save Image',fg='Blue', padx=1, pady=1,command=save_image_clicked)
save_button.pack()
save_button.place(relx=0.025, rely=0.85)

exit_button=tk.Button(frame,text='Exit',fg='Blue', padx=5, pady=2,command=exit_btn_clicked)
exit_button.pack()
exit_button.place(relx=0.85, rely=0.85)


canvas.pack()
root.mainloop()
