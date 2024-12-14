from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        #=========== variable ============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sc=StringVar()
        self.var_sa=StringVar()
        self.var_pass=StringVar()
        self.var_spass=StringVar()
        

        # first image
        img3=Image.open(r"C:\Users\moon\Desktop\project\images\moon1.jpg")
        img3=img3.resize((1500,750))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1500,height=750)

        frame=Frame(self.root,bg="white")
        frame.place(x=370,y=100,width=800,height=550)

        title_lbl=Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=20,y=20)
        
        #====== label and entry===========
        UNAME=Label(frame,text="First Name", font=("times new roman",15,"bold"),bg="white")
        UNAME.place(x=50,y=100)
        UNAME_E=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        UNAME_E.place(x=50,y=130,width=250)

        UNAME=Label(frame,text="Last Name", font=("times new roman",15,"bold"),bg="white")
        UNAME.place(x=370,y=100)
        self.UNAME_E1=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.UNAME_E1.place(x=370,y=130,width=250)

        A1=Label(frame,text="Contact No", font=("times new roman",15,"bold"),bg="white",fg="black")
        A1.place(x=50,y=170)
        self.A11=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.A11.place(x=50,y=200,width=250)

        A2=Label(frame,text="Email", font=("times new roman",15,"bold"),bg="white",fg="black")
        A2.place(x=370,y=170)
        self.A22=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.A22.place(x=370,y=200,width=250)

        A6=Label(frame,text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
        A6.place(x=50,y=240)
        self.A6_combo=ttk.Combobox(frame,textvariable=self.var_sc,font=("times new roman",13,"bold"),state="readonly",width=17)
        self.A6_combo["values"]=("Select","Your birth place","Favourite Person name")
        self.A6_combo.current(0)
        self.A6_combo.place(x=50,y=270,width=250)
        

        A3=Label(frame,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
        A3.place(x=370,y=240)
        self.A33=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.A33.place(x=370,y=270,width=250)

        A4=Label(frame,text="Passward", font=("times new roman",15,"bold"),bg="white",fg="black")
        A4.place(x=50,y=310)
        self.A44=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.A44.place(x=50,y=340,width=250)

        A5=Label(frame,text="Conform Passward", font=("times new roman",15,"bold"),bg="white",fg="black")
        A5.place(x=370,y=310)
        self.A55=ttk.Entry(frame,textvariable=self.var_spass,font=("times new roman",15,"bold"))
        self.A55.place(x=370,y=340,width=250)

        #=============check button============
        self.var_check=IntVar()
        chkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Term and Condition",font=("times new roman",13,"bold"),onvalue=1,offvalue=0)
        chkbtn.place(x=50,y=390)
        #=============Button===============
        
        b1_2=Button(frame,text="Register Now",command=self.register_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=10,y=440,width=250,height=50)

        b1_3=Button(frame,text="Login Now",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=370,y=440,width=250,height=50)

        

    #============function decleration=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sc.get()=="select":
            messagebox.showerror("Error","All Field are Required")
        elif self.var_pass.get()!=self.var_spass.get():
            messagebox.showerror("Error","passward & confirm passward must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our term and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from Register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another email")
            else:
                mycursor.execute("insert into Register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_sc.get(),
                                                                                        self.var_sa.get(),
                                                                                        self.var_pass.get(),
                                                                                     )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

            


            







if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()