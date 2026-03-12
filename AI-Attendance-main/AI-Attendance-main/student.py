from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import customtkinter as ctk
from time import strftime
from datetime import datetime

class Student:
     def __init__(self, root):
        self.root = root
        self.root.geometry("1400x720+0+0")
        self.root.title("Face Recognition System")
          # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        
    
        # First Image
        img = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\images (2).jpeg")
        img = img.resize((700, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img) 
        
        f_lbl = Label(self.root, image=self.photoimg) #RESIZE IMAGE
        f_lbl.place(x=0, y=0, width=700, height=130)
        
        # Second Image
        img1 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\download.jpeg")
        img1 = img1.resize((300, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1) 
        
        f_lbl = Label(self.root, image=self.photoimg1) #RESIZE IMAGE
        f_lbl.place(x=600, y=0, width=300, height=130)
        
        # Third Image
        
        img2 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\images (8).jpeg")
        img2 = img2.resize((700, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        
        f_lbl = Label(self.root, image=self.photoimg2) #RESIZE IMAGE
        f_lbl.place(x=900, y=0, width=700, height=130)
        

        # bg image
        img3 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\Admin block.jpg")
        img3 = img3.resize((1540, 720), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3) 
        
        bg_img = Label(self.root, image=self.photoimg3) #RESIZE IMAGE
        bg_img.place(x=0, y=130, width=1500, height=620)
        
        #Title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Arial", 35, "bold"), bg="white", fg="Black")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=550)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
        Left_frame.place(x=10,y=5,width=660,height=500)
        
        img_left= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\Admin block.jpg")
        img_left= img.resize((645, 110), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left) 
        
        f_lbl = Label(Left_frame, image=self.photoimg_left) #RESIZE IMAGE
        f_lbl.place(x=5, y=0, width=645, height=90)
        
        #current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("Arial",12,"bold"))
        current_course_frame.place(x=5,y=90,width=645,height=120)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("Arial",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Arial",12,"bold"),width=17,state="read only")
        dept_combo["values"]=("Select Department","CSE","ETE","ECE","ASE","ME","CH")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("Arial",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Arial",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

       

        #Year
        year_label=Label(current_course_frame,text="Year",font=("Arial",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Arial",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("Arial",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Arial",12,"bold"),width=17,state="read only")
        Semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Arial",12,"bold"))
        class_student_frame.place(x=5,y=210,width=645,height=260)

        #Student ID
        Studentid_label=Label(class_student_frame,text="Student ID:",font=("Arial",12,"bold"),bg="white")
        Studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17,font=("Arial",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        Studentname_label=Label(class_student_frame,text="Student Name:",font=("Arial",12,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17,font=("Arial",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("Arial",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=17,font=("Arial",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Arial",12,"bold"),width=15,state="read only")
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #Roll no
        roll_no__label=Label(class_student_frame,text="Roll no:",font=("Arial",12,"bold"),bg="white")
        roll_no__label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=17,font=("Arial",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("Arial",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=17,font=("Arial",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Arial",12,"bold"),width=15,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        #DOB
        DOB_label=Label(class_student_frame,text="DOB:",font=("Arial",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17,font=("Arial",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:",font=("Arial",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("Arial",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #Phone
        phone_label=Label(class_student_frame,text="Phone No:",font=("Arial",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=17,font=("Arial",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_student_frame,text="Address:",font=("Arial",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=17,font=("Arial",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher name:",font=("Arial",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17,font=("Arial",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio button
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame=LabelFrame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=197,width=604,height=35)

        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,command=self.update,text="Update",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="TakePhoto",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)

        update_photo_btn=Button(btn_frame,text="UpdatePhoto",width=9,font=("Arial",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=5)


        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
        Right_frame.place(x=680,y=5,width=800,height=500)

        img_right= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\images (8).jpeg")
        img_right= img_right.resize((770, 110), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right) 
        
        f_lbl = Label(Right_frame, image=self.photoimg_right) #RESIZE IMAGE
        f_lbl.place(x=5, y=0, width=770, height=90)
        
        # Search Frame
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Arial",12,"bold"))
        Search_frame.place(x=0,y=100,width=790,height=80)
        
        Search_label=Label(Search_frame,text="Search by",font=("Helvetica",12,"bold"),bg="green",fg = "white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Search_combo=ttk.Combobox(Search_frame,font=("Arial",12,"bold"),width=17,state="read only")
        Search_combo["values"]=("Select Student By","Roll No","Name")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame,width=17,font=("Helvetica",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=9,font=("Helvetica",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        ShowAll_btn=Button(Search_frame,text="Show All",width=9,font=("Helvetica",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4)
        
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=3,y=185,width=790,height=250)
        
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.StudentTable = ttk.Treeview(Table_frame,column = ('dep','course','year','sem','id','name','sec','roll','gender','dob','email','phone','address','teacher','photostat'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side= BOTTOM,fill=X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        
        self.StudentTable.heading("dep",text = "Department")
        self.StudentTable.heading("course",text = "Course")
        self.StudentTable.heading("year",text = "Year")
        self.StudentTable.heading("sem",text = "Semester")
        self.StudentTable.heading("id",text = "ID NO")
        self.StudentTable.heading("name",text = "Name")
        self.StudentTable.heading("sec",text = "Section")
        self.StudentTable.heading("roll",text = "Roll No")
        self.StudentTable.heading("gender",text = "Gender") 
        self.StudentTable.heading("dob",text = "Date Of Birth") 
        self.StudentTable.heading("email",text = "Email") 
        self.StudentTable.heading("phone",text = "Phone") 
        self.StudentTable.heading("address",text = "Address")
        self.StudentTable.heading("teacher",text = "Teacher")  
        self.StudentTable.heading("photostat",text = "Photo Status")       
         
        self.StudentTable["show"] = "headings"
        
        self.StudentTable.column("dep",width=100)
        self.StudentTable.column("course",width=100)
        self.StudentTable.column("year",width=100)
        self.StudentTable.column("sem",width=100)
        self.StudentTable.column("id",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("photostat",width=150)
        self.StudentTable.column("sec",width=100)
        self.StudentTable.column("address",width=300)
        
        
        
        
        
        self.StudentTable.pack(fill=BOTH,expand=1) 
        self.StudentTable.bind("<ButtonRelease>",self.get_cursor)  
        self.fetch_data()
        
        # function declaration
     def add_data(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_roll.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                  try:
                      conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
                      my_cursor = conn.cursor()
                      my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                          ))
                      conn.commit()
                      self.fetch_data()
                      conn.close()
                      messagebox.showinfo("Success","Data Added Sucessfully",parent=self.root)
                  except Exception as es:
                      messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
#  fetch data function
     def fetch_data(self):
       conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
       my_cursor = conn.cursor()
       my_cursor.execute("select * from student")
       data = my_cursor.fetchall()
       if len(data) !=0:
           self.StudentTable.delete(*self.StudentTable.get_children())
       for i in data:
         self.StudentTable.insert("",END,values=i)
       conn.commit()
       conn.close() 
# get cursor function
     def get_cursor(self,event=""):
       cursor_focus = self.StudentTable.focus()
       content = self.StudentTable.item(cursor_focus)
       data = content["values"]
       
       self.var_dep.set(data[0])
       self.var_course.set(data[1])
       self.var_year.set(data[2])
       self.var_semester.set(data[3])
       self.var_std_id.set(data[4])
       self.var_std_name.set(data[5])
       self.var_div.set(data[6])
       self.var_roll.set(data[7])
       self.var_gender.set(data[8])
       self.var_dob.set(data[9])
       self.var_email.set(data[10])
       self.var_phone.set(data[11])
       self.var_address.set(data[12])
       self.var_teacher.set(data[13])
       self.var_radio1.set(data[14])
       
#  Update function
     def update(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_roll.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
              Update = messagebox.askyesno("Update","Do you want to update the details?",parent=self.root)
              if Update>0:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("update student set department=%s,course = %s,year=%s,semester=%s,Name=%s,division=%s,roll=%s,gender=%s,DOB=%s,email=%s,phone_no=%s,address=%s,teacher_name=%s,photo_sample=%s where Student_id = %s",(
                  self.var_dep.get(),
                  self.var_course.get(),
                  self.var_year.get(),
                  self.var_semester.get(),
                  self.var_std_name.get(),
                  self.var_div.get(),
                  self.var_roll.get(),
                  self.var_gender.get(),
                  self.var_dob.get(),
                  self.var_email.get(),
                  self.var_phone.get(),
                  self.var_address.get(),
                  self.var_teacher.get(),
                  self.var_radio1.get(),
                  self.var_std_id.get()
                ))
              else:
                if not Update:
                  return
              messagebox.showinfo("Success","Updated Sucessfully!")    
              conn.commit()
              self.fetch_data()
              conn.close()    
            except Exception as es:
              messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
              
# delete Data
     def delete_data(self):   
       if self.var_std_id.get() == "":
         messagebox.showerror("Error","Student ID not defined",parent=self.root)
       else:
        try:
          delete=messagebox.askyesno("Confirm","Do you want to delete this data?")
          if delete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
            my_cursor = conn.cursor()
            sql = "delete from student where Student_id=%s"
            val = (self.var_std_id.get(),)
            my_cursor.execute(sql,val)
          else:
            if not delete:
              return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success","Student Information Deleted Sucessfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)  
            
# reset function            
     def reset_data(self):
                  self.var_dep.set("Select Department"),
                  self.var_course.set("Select Course"),
                  self.var_year.set("Select Year"),
                  self.var_semester.set("Select Semester"),
                  self.var_std_name.set(""),
                  self.var_div.set(""),
                  self.var_roll.set(""),
                  self.var_gender.set(" "),
                  self.var_dob.set(" "),
                  self.var_email.set(" "),
                  self.var_phone.set(" "),
                  self.var_address.set(""),
                  self.var_teacher.set(""),
                  self.var_radio1.set(""),
                  self.var_std_id.set("")
      #===========Generate data set or Take Photo Samples============mohsin code
    #  def generate_dataset(self):
    #     if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
    #         messagebox.showerror("Error","All Fields are required")
    #     else:
    #         try:

    #             conn=mysql.connector.connect(host="localhost",username="root",password="Sahil&@80085",database="face_recognizer")
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("Select * from student")
    #             myresult=my_cursor.fetchall()
    #             id=0
    #             for x in myresult:
    #                 id+=1
    #             my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,Name=%s,division=%s,roll=%s,gender=%s,DOB=%s,email=%s,phone_no=%s,address=%s,teacher_name=%s,photo_sample=%s where Student_id=%s",(

    #                                                                                                                                                                                 self.var_dep.get(),
    #                                                                                                                                                                                 self.var_course.get(),
    #                                                                                                                                                                                 self.var_year.get(),
    #                                                                                                                                                                                 self.var_semester.get(),
    #                                                                                                                                                                                 self.var_std_name.get(),
    #                                                                                                                                                                                 self.var_div.get(),
    #                                                                                                                                                                                 self.var_roll.get(),
    #                                                                                                                                                                                 self.var_gender.get(),
    #                                                                                                                                                                                 self.var_dob.get(),
    #                                                                                                                                                                                 self.var_email.get(),
    #                                                                                                                                                                                 self.var_phone.get(),
    #                                                                                                                                                                                 self.var_address.get(),
    #                                                                                                                                                                                 self.var_teacher.get(),
    #                                                                                                                                                                                 self.var_radio1.get(),
    #                                                                                                                                                                                 self.var_std_id.get()))
    #             conn.commit()
    #             self.fetch_data()
    #             self.reset_data()
    #             conn.close

    #             #===============Load predefined data on face fontals from opencv===========
    #             face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #             def face_cropped(img):
    #                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #                 faces=face_classifier.detectMultiScale(gray,1.3,5)
    #                 #scaling factor=1.3
    #                 #Minimum Neighbor=5
    #                 for (x,y,w,h) in faces:
    #                     face_cropped=img[y:y+h,x:x+w]
    #                     return face_cropped
    #             cap=cv2.VideoCapture(0)
    #             img_id=0
    #             while True:
    #                 ret,my_frame=cap.read()
    #                 if face_cropped(my_frame) is not None:
    #                     img_id+=1
    #                 face=cv2.resize(face_cropped(my_frame),(450,450))
    #                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    #                 file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
    #                 cv2.imwrite(file_name_path)
    #                 cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    #                 cv2.imshow("Cropped Face",face)

    #                 if cv2.waitKey(1)==13 or int(img_id)==100:
    #                     break
    #             cap.release()
    #             cv2.destroyAllWindows()
    #             messagebox.showinfo("Result","Generating data sets completed!!!!!")
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
     def generate_dataset(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All Fields are required")
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Select * from student")
                    myresult = my_cursor.fetchall()
                    id_counter = 0
                    for x in myresult:
                        id_counter += 1
                    my_cursor.execute(
                        "update student set department=%s, course=%s, year=%s, semester=%s, Name=%s, division=%s, roll=%s, gender=%s, DOB=%s, email=%s, phone_no=%s, address=%s, teacher_name=%s, photo_sample=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # Load the Haar cascade for face detection (adjust path if necessary)
                    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            cropped_face = img[y:y+h, x:x+w]
                            return cropped_face
                        return None

                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    while True:
                        ret, my_frame = cap.read()
                        if not ret:
                            break  # Break if frame not read properly

                        cropped_face = face_cropped(my_frame)
                        if cropped_face is not None:
                            img_id += 1
                            # Resize and convert to grayscale
                            try:
                                face = cv2.resize(cropped_face, (450, 450))
                            except Exception as e:
                                print("Error resizing face:", e)
                                continue
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            file_name_path = "data/user." + str(id_counter) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 50:  # 13 is the Enter key
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed!!!!!")
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
           


               
              
            
            
            
         
            
                 
                

       
            

        
      
                      
                    
                
                           
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()