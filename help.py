from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from students  import Student 
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK", font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top=Image.open(r"C:\Users\moon\Desktop\project\images\desk.jpg")
        img_top=img_top.resize((1500,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1500,height=700)

        dev_label=Label(f_lbl,text="Email:abc@gmail.com",font=("times new roman",40,"bold"),fg="darkblue",bg="white")
        dev_label.place(x=470,y=300)

        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()