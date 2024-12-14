from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")
        self.root.title("Face Recognition System")

        #==========variable============================
        self.var_a_rollno=StringVar()
        self.var_a_name=StringVar()
        self.var_a_department=StringVar()
        self.var_a_time=StringVar()
        self.var_a_date=StringVar()
        self.var_a_attend=StringVar()
        # first image
        img=Image.open(r"C:\Users\moon\Desktop\project\images\stud1.jpg")
        img=img.resize((750,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=750,height=200)

        # second image
        img1=Image.open(r"C:\Users\moon\Desktop\project\images\stud4.jpg")
        img1=img1.resize((750,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=750,y=0,width=750,height=200)

        title_lbl=Label(self.root,text="ATTENDANCE  MANAGEMENT  SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=200,width=1500,height=45)

        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10,y=250,width=1470,height=490 )
      
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=720,height=480)

        img_left=Image.open(r"C:\Users\moon\Desktop\project\images\dev2.jfif")
        img_left=img_left.resize((710,180))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=180)

        # current frame
        lf_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current  Information",font=("times new roman",12,"bold"))
        lf_frame.place(x=5,y=205,width=710,height=235)

        #labels and enteries
        # attendance rollno
        stuR_label=Label(lf_frame,text="Roll No:",font=("times new roman",13,"bold"))
        stuR_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        R_entry=ttk.Entry(lf_frame,textvariable=self.var_a_rollno,width=22,font=("times new roman",13,"bold"))
        R_entry.grid(row=0,column=1,padx=10,pady=7,sticky=W)

        #  name
        stuN_label=Label(lf_frame,text=" Name:",font=("times new roman",13,"bold"))
        stuN_label.grid(row=0,column=2,padx=10,pady=7,sticky=W)

        N_entry=ttk.Entry(lf_frame,textvariable=self.var_a_name,width=20,font=("times new roman",13,"bold"))
        N_entry.grid(row=0,column=3,padx=10,pady=7,sticky=W)

        #  Date
        stuN_label=Label(lf_frame,text=" Date:",font=("times new roman",13,"bold"))
        stuN_label.grid(row=2,column=0,padx=10,pady=7,sticky=W)

        N_entry=ttk.Entry(lf_frame,textvariable=self.var_a_date,width=22,font=("times new roman",13,"bold"))
        N_entry.grid(row=2,column=1,padx=10,pady=7,sticky=W)

        #  Time
        stuN_label=Label(lf_frame,text=" Time:",font=("times new roman",13,"bold"))
        stuN_label.grid(row=1,column=2,padx=10,pady=7,sticky=W)

        N_entry=ttk.Entry(lf_frame,textvariable=self.var_a_time,width=20,font=("times new roman",13,"bold"))
        N_entry.grid(row=1,column=3,padx=10,pady=7,sticky=W)

        #  Dep
        stuN_label=Label(lf_frame,text=" Department:",font=("times new roman",13,"bold"))
        stuN_label.grid(row=1,column=0,padx=10,pady=7,sticky=W)

        N_entry=ttk.Entry(lf_frame,textvariable=self.var_a_department,width=22,font=("times new roman",13,"bold"))
        N_entry.grid(row=1,column=1,padx=10,pady=7,sticky=W)

        #Attendence 
        Att_label=Label(lf_frame,text="Attendance status",font=("times new roman",13,"bold"))
        Att_label.grid(row=2,column=2,padx=10,sticky=W)

        Att_combo=ttk.Combobox(lf_frame,textvariable=self.var_a_attend,font=("times new roman",13,"bold"),state="readonly",width=17)
        Att_combo["values"]=("Status","Present","Absent")
        Att_combo.current(0)
        Att_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        # Button frame
        btn_frame=Frame(lf_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=700,height=35)
         
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=23,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        import_btn.grid(row=0,column=0)
    
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=22,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        export_btn.grid(row=0,column=1)
    
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=22,height=1,font=("times new roman",13,"bold"),fg="white",bg="green")
        reset_btn.grid(row=0,column=3)

        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=5,width=720,height=480)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=450)

        #==========scroll bar or table============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attReport=ttk.Treeview(table_frame,column=("rollno","name","department","time","date","attendance"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attReport.xview)
        scroll_y.config(command=self.attReport.yview)

        self.attReport.heading("rollno",text="Roll No")
        self.attReport.heading("name",text="Name")
        self.attReport.heading("department",text="Department")
        self.attReport.heading("time",text="Time")
        self.attReport.heading("date",text="Date")
        self.attReport.heading("attendance",text="Attendance")

        self.attReport["show"]="headings"
        self.attReport.column("rollno",width=100)
        self.attReport.column("name",width=100)
        self.attReport.column("department",width=100)
        self.attReport.column("time",width=100)
        self.attReport.column("date",width=100)
        self.attReport.column("attendance",width=100)

        self.attReport.pack(fill=BOTH,expand=1)

        self.attReport.bind("<ButtonRelease>",self.get_cursor)

#=============== fetch data =============================
    def fetchData(self,rows):
        self.attReport.delete(*self.attReport.get_children())
        for i in rows:
            self.attReport.insert("",END,values=i)

    #import csv    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv 
    def exportCsv(self):
        try:
            if len(mydata)>=1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimeter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                  messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
   
                     
    def get_cursor(self,event=""):
        cursor_row=self.attReport.focus()
        content=self.attReport.item(cursor_row)
        rows=content['values']
        self.var_a_rollno.set(rows[0])
        self.var_a_name.set(rows[1])
        self.var_a_department.set(rows[2])
        self.var_a_time.set(rows[3])
        self.var_a_date.set(rows[4])
        self.var_a_attend.set(rows[5])

    def reset_data(self):
        self.var_a_rollno.set("")
        self.var_a_name.set("")
        self.var_a_department.set("")
        self.var_a_time.set("")
        self.var_a_date.set("")
        self.var_a_attend.set("")
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()