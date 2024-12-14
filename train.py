from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top=Image.open(r"C:\Users\moon\Desktop\project\images\istockphoto-1465476073-2048x2048.jpg")
        img_top=img_top.resize((1500,320))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1500,height=320)

        btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="green",fg="white")
        btn.place(x=0,y=368,width=1500,height=60)

        img_bottom=Image.open(r"C:\Users\moon\Desktop\project\images\stud1.jpg")
        img_bottom=img_bottom.resize((1500,320))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=430,width=1500,height=320)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grey scale image
            imageNp=np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
              
 
        ids=np.array(ids)
        
        #=========Train the Classifier==========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")  # save trianing data
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")
    
if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()