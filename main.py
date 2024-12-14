from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
import tkinter
from tkinter import messagebox
from time import strftime
from datetime import datetime
from developer import Developer1
from students  import Student 
from train import train
from recognition import Recognition
from attendance import Attendance
from help import Help
import mysql.connector
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        # first image
        img=Image.open(r"C:\Users\moon\Desktop\project\images\face.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"C:\Users\moon\Desktop\project\images\istockphoto-1465476073-2048x2048.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"C:\Users\moon\Desktop\project\images\face.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # big image
        img3=Image.open(r"C:\Users\moon\Desktop\project\images\istockphoto-175448547-612x612.jpg")
        img3=img3.resize((1500,620))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=620)

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        # student button
        img4=Image.open(r"C:\Users\moon\Desktop\project\images\istockphoto-485376695-612x612.jpg")
        img4=img4.resize((200,200))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.stud,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.stud,cursor="hand2",font=("times new roman",15,"bold"),activebackground="green",
                    activeforeground="white",bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=200,height=40)

        # Detect the face
        img5=Image.open(r"C:\Users\moon\Desktop\project\images\istockphoto-1344147937-2048x2048.jpg")
        img5=img5.resize((200,200))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.recog,cursor="hand2")
        b1.place(x=500,y=100,width=200,height=200)

        b1_2=Button(bg_img,text="Face Detector",command=self.recog,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=500,y=300,width=200,height=40)


        # Attendance face button
        img6=Image.open(r"C:\Users\moon\Desktop\project\images\a.jpg")
        img6=img6.resize((200,200))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attend,cursor="hand2")
        b1.place(x=800,y=100,width=200,height=200)

        b1_3=Button(bg_img,text="Attendance",command=self.attend,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=800,y=300,width=200,height=40)
        
        
        # Help face button
        img7=Image.open(r"C:\Users\moon\Desktop\project\images\desk2.jpg")
        img7=img7.resize((200,200))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help,cursor="hand2")
        b1.place(x=1100,y=100,width=200,height=200)

        b1_3=Button(bg_img,text="Help Desk",command=self.help,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=1100,y=300,width=200,height=40)
        

        # Train data button
        img8=Image.open(r"C:\Users\moon\Desktop\project\images\istockphoto-1176067266-2048x2048.jpg")
        img8=img8.resize((200,200))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train,cursor="hand2")
        b1.place(x=200,y=370,width=200,height=200)

        b1_3=Button(bg_img,text="Train Data",command=self.train,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=200,y=550,width=200,height=40)
        

        # Photos button
        img9=Image.open(r"C:\Users\moon\Desktop\project\images\att.jpg")
        img9=img9.resize((200,200))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=370,width=200,height=200)

        b1_3=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=500,y=550,width=200,height=40)
        

        # Developer  button
        img10=Image.open(r"C:\Users\moon\Desktop\project\images\developer2.jpg")
        img19=img10.resize((200,200))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.develop,cursor="hand2")
        b1.place(x=800,y=370,width=200,height=200)

        b1_3=Button(bg_img,text="Developer",command=self.develop,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=800,y=550,width=200,height=40)
        

        # Exit button
        img11=Image.open(r"C:\Users\moon\Desktop\project\images\exit.jpg")
        img11=img11.resize((200,200))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2")
        b1.place(x=1100,y=370,width=200,height=200)

        b1_3=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=1100,y=550,width=200,height=40)

    #========Photo function===========================
    def open_img(self):
        os.startfile("data")
    #==========exit function===========================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit window",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    #=============== Function button ====================
    def stud(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def develop(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer1(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()