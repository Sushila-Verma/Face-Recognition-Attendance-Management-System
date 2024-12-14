from tkinter import *
from tkinter import ttk
from winreg import QueryReflectionKey
from PIL import Image , ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        # first image
        img3=Image.open(r"C:\Users\moon\Desktop\project\images\moon.jpg")
        img3=img3.resize((1500,750))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1500,height=750)

        frame=Frame(self.root,bg="Black")
        frame.place(x=610,y=170,width=340,height=450)

        img2=Image.open(r"C:\Users\moon\Desktop\project\images\login.jpg")
        img2=img2.resize((100,100))
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img1=Label(frame,image=self.photoimg2)
        bg_img1.place(x=120,y=0,width=100,height=100)

        title_lbl=Label(frame,text="Get Started", font=("times new roman",20,"bold"),bg="black",fg="white")
        title_lbl.place(x=95,y=100)

        #label
        UNAME=Label(frame,text="Username", font=("times new roman",15,"bold"),bg="black",fg="white")
        UNAME.place(x=75,y=155)
        self.UNAME=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.UNAME.place(x=40,y=180,width=270)

        UPASS=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="black",fg="white")
        UPASS.place(x=75,y=225)
        self.UPASS=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.UPASS.place(x=40,y=250,width=270)

        #============icon image===========================
        img5=Image.open(r"C:\Users\moon\Desktop\project\images\login.jpg")
        img5=img5.resize((25,25))
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_img5=Label(frame,image=self.photoimg5)
        bg_img5.place(x=50,y=155,width=25,height=25)

        img4=Image.open(r"C:\Users\moon\Desktop\project\images\picon.png")
        img4=img4.resize((25,25))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img4=Label(frame,image=self.photoimg4)
        bg_img4.place(x=50,y=225,width=25,height=25)
         # login button
        b1_1=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,activebackground="green",activeforeground="white",bg="green",fg="white")
        b1_1.place(x=110,y=300,width=120,height=35)

        #register button
        b1_1=Button(frame,text="New User Password",command=self.Register_window,font=("times new roman",12,"bold"),borderwidth=0,activebackground="green",activeforeground="white"
                    ,bg="black",fg="white")
        b1_1.place(x=30,y=350,width=160)

        #forget passward button
        b1_1=Button(frame,text="Forget Password",command=self.forget_pass_win,font=("times new roman",12,"bold"),borderwidth=0,activebackground="green",
                    activeforeground="white",bg="black",fg="white")
        b1_1.place(x=23,y=370,width=160)

    def Register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
       
    def login(self):   
        if self.UNAME.get()=="" or self.UNAME.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.UPASS.get()=="kapu" or self.UPASS.get()=="aashu":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
            mycursor=conn.cursor()
            mycursor.execute("Select * from Register where email=%s and password=%s",(
                                                                                    self.UNAME.get(),
                                                                                    self.UPASS.get()
                                                                                ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #=========Reset Passward===================
    def reset(self):
        if self.A6_combo.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.A33.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.Anew_p1.get()=="":
            messagebox.showerror("Error","Please Enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
            mycursor=conn.cursor()
            query1=("select * from Register where email=%s and securityQ=%s and securityA=%s")
            value1=(self.UNAME.get(),self.A6_combo.get(),self.A33.get(),)
            mycursor.execute(query1,value1)
            row=mycursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query2=("update Register set passward=%s where email=%s")
                value2=(self.Anew_p1.get(),self.UNAME.get())
                mycursor.execute(query2,value2)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password hasbeen reset, Please login new Password",parent=self.root2)
                self.root2.destroy()

    #============ forget passward================
    def forget_pass_win(self):
        if self.UNAME.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from Register where email=%s")
            value=(self.UNAME.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                lbl=Label(self.root2,text="Forget Passward", font=("times new roman",20,"bold"),bg="white",fg="darkgreen")
                lbl.place(x=0,y=10,relwidth=1) 

                A6=Label(self.root2,text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
                A6.place(x=50,y=80)
                self.A6_combo=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly",width=17)
                self.A6_combo["values"]=("Select","Your birth place","Favourite Person name")
                self.A6_combo.current(0)
                self.A6_combo.place(x=50,y=110,width=250)
                
                A3=Label(self.root2,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
                A3.place(x=50,y=150)
                self.A33=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.A33.place(x=50,y=180,width=250) 

                new_p=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_p.place(x=50,y=220)
                self.Anew_p1=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.Anew_p1.place(x=50,y=250,width=250) 

                b1=Button(self.root2,text="Reset",command=self.reset,font=("times new roman",15,"bold"),bd=3,bg="green",fg="white")
                b1.place(x=110,y=300)

#==========Register class===================
                    
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

        A4=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        A4.place(x=50,y=310)
        self.A44=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.A44.place(x=50,y=340,width=250)

        A5=Label(frame,text="Conform Password", font=("times new roman",15,"bold"),bg="white",fg="black")
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

        b1_3=Button(frame,text="Login Now",command=self.return_login,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
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

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()