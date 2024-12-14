from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from students  import Student 
from tkinter import messagebox
import mysql.connector
import cv2

class Developer1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top=Image.open(r"C:\Users\moon\Desktop\project\images\developer.jpg")
        img_top=img_top.resize((1500,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1500,height=700)
        
        #frame

        main_f = Frame(f_lbl,bd=2,bg="white")
        main_f.place(x=350,y=100,width=850,height=500)

        img_n=Image.open(r"C:\Users\moon\Desktop\project\images\student2.png")
        img_n=img_n.resize((220,220))
        self.photoimg_n=ImageTk.PhotoImage(img_n)

        f_lbl=Label(main_f,image=self.photoimg_n)
        f_lbl.place(x=0,y=0,width=220,height=220)

        img_h=Image.open(r"C:\Users\moon\Desktop\project\images\R.jfif")
        img_h=img_h.resize((220,220))
        self.photoimg_h=ImageTk.PhotoImage(img_h)

        f_lbl=Label(main_f,image=self.photoimg_h)
        f_lbl.place(x=323,y=0,width=220,height=220)

        
        img_s=Image.open(r"C:/Users/moon/Desktop/project/images/student2.png")
        img_s=img_s.resize((220,220))
        self.photoimg_s=ImageTk.PhotoImage(img_s)

        f_lbl=Label(main_f,image=self.photoimg_s)
        f_lbl.place(x=630,y=0,width=220,height=220)


        # developer info
        dev_label=Label(main_f,text="Hello!! My name Sushila...",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=240)

        dev_labe3=Label(main_f,text="I am student of MCA (2nd) from Chaudhary Ranbir Singh University , ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_labe3.place(x=0,y=280)

        dev_label=Label(main_f,text="Jind (Haryana)...",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=320)

        dev_label=Label(main_f,text="My Course is about Data Science...",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=360)

        
if __name__ == "__main__":
    root=Tk()
    obj=Developer1(root)
    root.mainloop()