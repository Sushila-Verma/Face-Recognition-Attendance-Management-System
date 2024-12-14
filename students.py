from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        #=========== variable ============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_teacher=StringVar()
        
        # first image
        img=Image.open(r"C:\Users\moon\Desktop\project\images\stud1.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"C:\Users\moon\Desktop\project\images\stud4.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"C:\Users\moon\Desktop\project\images\stud3.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1470,height=600 )

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=550)

        img_left=Image.open(r"C:\Users\moon\Desktop\project\images\s1.jpg")
        img_left=img_left.resize((710,120))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=120)

        # current frame
        cc_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        cc_frame.place(x=5,y=125,width=710,height=120)

        # department
        dep_label=Label(cc_frame,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer","Science")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # course
        course_label=Label(cc_frame,text="Course",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(cc_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select course","Data Science","Web Development","Mathematics","Biology","chemistry","Physics","botony")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
 
        # year
        year_label=Label(cc_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
 
        # semester
        sem_label=Label(cc_frame,text="Semester",font=("times new roman",13,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(cc_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),state="readonly",width=17)
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


         # class student information
        cs_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        cs_frame.place(x=5,y=250,width=710,height=270)

         # Student ID
        stuID_label=Label(cs_frame,text="Student ID:",font=("times new roman",13,"bold"))
        stuID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(cs_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student name
        stuN_label=Label(cs_frame,text="Student Name:",font=("times new roman",13,"bold"))
        stuN_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        N_entry=ttk.Entry(cs_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        N_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Student rollno
        stuR_label=Label(cs_frame,text="Roll No:",font=("times new roman",13,"bold"))
        stuR_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        R_entry=ttk.Entry(cs_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        R_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Gender
        stuG_label=Label(cs_frame,text="Gender:",font=("times new roman",13,"bold"))
        stuG_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(cs_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gen_combo["values"]=("Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Email
        stuE_label=Label(cs_frame,text="Email:",font=("times new roman",13,"bold"))
        stuE_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        E_entry=ttk.Entry(cs_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        E_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # dob
        dob_label=Label(cs_frame,text="DOB:",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(cs_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Phone no
        stuID_label=Label(cs_frame,text="Phone No:",font=("times new roman",13,"bold"))
        stuID_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(cs_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",13,"bold"))
        id_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # teacher name
        stuT_label=Label(cs_frame,text="Teacher Name:",font=("times new roman",13,"bold"))
        stuT_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        T_entry=ttk.Entry(cs_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        T_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Radio button1
        self.var_radio1=StringVar()
        rd1=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        rd1.grid(row=6,column=0)

        #Radio button2
        rd2=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        rd2.grid(row=6,column=1)

       # Button frame
        btn_frame=Frame(cs_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=700,height=35)
         
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        save_btn.grid(row=0,column=0)
    
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        update_btn.grid(row=0,column=1)
    
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        reset_btn.grid(row=0,column=2)
    
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        delete_btn.grid(row=0,column=3)
    
        # Button frame1
        btn_fram1=Frame(cs_frame,bd=2,relief=RIDGE,bg="white")
        btn_fram1.place(x=0,y=205,width=700,height=35)
         
        tp_btn=Button(btn_fram1,command=self.gen_dataset,text="Take Photo Sample",width=30,height=1,font=("times new roman",15,"bold"),fg="white",bg="blue")
        tp_btn.grid(row=0,column=0)
    
        updatep_btn=Button(btn_fram1,text="Update Photo Sample",width=30,height=1,font=("times new roman",15,"bold"),fg="white",bg="blue")
        updatep_btn.grid(row=0,column=1)
        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=720,height=550)

        img_right=Image.open(r"C:\Users\moon\Desktop\project\images\vishu.jpg")
        img_right=img_right.resize((710,120))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=710,height=120)

          # ==========Search System ====================
        src_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        src_frame.place(x=5,y=125,width=710,height=60)

        # search by
        src_label=Label(src_frame,text="Search by:",font=("times new roman",13,"bold"),bg="red",fg="white")
        src_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(src_frame,textvariable=self.var_com_search,font=("times new roman",13,"bold"),state="readonly",width=17)
        search_combo["values"]=("Select","Roll No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        src_entry=ttk.Entry(src_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        src_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        src_btn=Button(src_frame,text="Search",command=self.search_data,width=12,height=1,font=("times new roman",12,"bold"),fg="white",bg="blue")
        src_btn.grid(row=0,column=3,padx=4)
        src_btn=Button(src_frame,text="show All",command=self.fetch_data,width=12,height=1,font=("times new roman",12,"bold"),fg="white",bg="blue")
        src_btn.grid(row=0,column=4,padx=4)

        #============== Table Frame ==============
        tb_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        tb_frame.place(x=5,y=190,width=710,height=330)

        scroll_x= ttk.Scrollbar(tb_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(tb_frame,orient=VERTICAL)

        self.stu_table=ttk.Treeview(tb_frame,column =("dep","course","year","sem","id","name","roll","gender","dob","phone_no","email","teacher","photo"),
                                    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

        self.stu_table.heading("dep",text="Department")
        self.stu_table.heading("course",text="Course")
        self.stu_table.heading("year",text="Year")
        self.stu_table.heading("sem",text="Semester")
        self.stu_table.heading("id",text="Student_ID")
        self.stu_table.heading("name",text="Name")
        self.stu_table.heading("roll",text="Roll No")
        self.stu_table.heading("gender",text="Gender")
        self.stu_table.heading("dob",text="DOB")
        self.stu_table.heading("phone_no",text="Phone_No")
        self.stu_table.heading("email",text="Email")
        self.stu_table.heading("teacher",text="Teacher")
        self.stu_table.heading("photo",text="Photo_sample_status")
        self.stu_table["show"]="headings"

        self.stu_table.column("dep",width=100)
        self.stu_table.column("course",width=100)
        self.stu_table.column("year",width=100)
        self.stu_table.column("sem",width=100)
        self.stu_table.column("id",width=100)
        self.stu_table.column("name",width=100)
        self.stu_table.column("roll",width=100)
        self.stu_table.column("gender",width=100)
        self.stu_table.column("dob",width=100)
        self.stu_table.column("phone_no",width=100)
        self.stu_table.column("email",width=100)
        self.stu_table.column("teacher",width=100)
        self.stu_table.column("photo",width=100)

        self.stu_table.pack(fill=BOTH,expand=1)
        self.stu_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #================= function decleration================
   
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                     self.var_dep.get(),
                                                                                                     self.var_course.get(),
                                                                                                     self.var_year.get(),
                                                                                                     self.var_sem.get(),
                                                                                                     self.var_id.get(),
                                                                                                     self.var_name.get(),
                                                                                                     self.var_roll.get(),
                                                                                                     self.var_gender.get(),
                                                                                                     self.var_dob.get(),
                                                                                                     self.var_phone_no.get(),
                                                                                                     self.var_email.get(),
                                                                                                     self.var_teacher.get(),
                                                                                                     self.var_radio1.get()
                                                                                                 )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

        
    #=============fatch data ====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
        mycursor=conn.cursor()
        mycursor.execute("select * from student1")
        data=mycursor.fetchall()

        if len(data) != 0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in data:
                self.stu_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===========  get cursor ====================    
    def get_cursor(self,event=""):
        cursor_focus=self.stu_table.focus()
        content=self.stu_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_phone_no.set(data[9]),
        self.var_email.set(data[10]),
        self.var_teacher.set(data[11]),   
        self.var_radio1.set(data[12]),
        
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
                    mycursor=conn.cursor()
                    mycursor.execute("""UPDATE student1 SET Dep=%s,Course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Gender=%s,DOB=%s,Phone_no=%s,Email=%s,Teacher=%s,photo=%s 
                                         WHERE Roll_No=%s
                                         """,(
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_sem.get(),
                                                self.var_id.get(),
                                                self.var_name.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_phone_no.get(),
                                                self.var_email.get(),
                                                self.var_teacher.get(),
                                                self.var_radio1.get(),
                                                self.var_roll.get()
                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#delete data
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll_no must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
                    mycursor=conn.cursor()
                    sql="Delete from student1 where Roll_No=%s"
                    val=(self.var_roll.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # Search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("Select * from student1 where Roll_No "+" LIKE '%"+str(self.var_search.get())+"%'")
                data=mycursor.fetchall()
                if len(data)!=0:
                    self.stu_table.delete(*self.stu_table.get_children())
                    for i in data:
                        self.stu_table.insert("",END,values=i)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
# ============= Generate data set or Take photo sample ====================
    def gen_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sv75@68980#",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("select * from student1")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycursor.execute("UPDATE student1 set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Gender=%s,DOB=%s,Phone_no=%s,Email=%s,Teacher=%s,photo=%s WHERE Roll_No=%s",(
                        
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                self.var_id.get(),
                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_phone_no.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_roll.get()==id+1
                                                                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=============load predefined data on face frontals from opencv ======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()