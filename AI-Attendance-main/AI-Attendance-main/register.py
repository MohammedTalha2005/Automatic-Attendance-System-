from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

# variable declaration



class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800+0+0")
        self.root.title("Register New User")
        #variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        
         # Background Image
        img = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\bg-image.jpg")
        self.bg = ImageTk.PhotoImage(img)
        
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=-40,y=0,height=800, width=1600)  

        # Login Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=400, y=100, width=800,height=600)
        
        #Register Label
        register_lbl = Label(frame,text="Register A new User", font=("times new roman", 20, "bold"),fg="green", bg="white")
        register_lbl.place(x=50, y=50)
        
        # first name Label
        fname_lbl = Label(frame, text="First Name:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        fname_lbl.place(x=50, y=150)
    
        # first name Entry Field
        self.txt_fname = Entry(frame,textvariable=self.var_fname, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=180, width=250, height=35)
        
        # Contact Label
        contact_lbl = Label(frame,text="Contact No:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        contact_lbl.place(x=50, y=220)
        
        # contact Entry Field
        self.txt_contact = Entry(frame,textvariable=self.var_contact , font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=250, width=250, height=35)
        
        #last name label
        lname_lbl = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        lname_lbl.place(x=450, y=150)
        self.txt_lname = Entry(frame,textvariable=self.var_lname, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=450, y=180, width=250, height=35)
        
        #email Label
        email_lbl = Label(frame, text="Email:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        email_lbl.place(x=450, y=220)
        self.txt_email = Entry(frame,textvariable=self.var_email , font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=450, y=250, width=250, height=35)
        
        #security question label
        security_lbl = Label(frame, text="Security Question:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        security_lbl.place(x=50, y=300)
        self.cmb_quest = ttk.Combobox(frame,textvariable=self.var_securityQ , font=("times new roman", 13), state='readonly', justify=CENTER)    
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=330, width=250, height=35)
        self.cmb_quest.current(0)
        
        #security answer label
        answer_lbl = Label(frame, text="Answer:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        answer_lbl.place(x=450, y=300)
        self.txt_answer = Entry(frame,textvariable=self.var_securityA , font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=450, y=330, width=250, height=35)
        
        #username Label
        username_lbl = Label(frame, text="Username:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        username_lbl.place(x=50, y=370)
        self.txt_username = Entry(frame,textvariable=self.var_username , font=("times new roman", 15), bg="lightgray")
        self.txt_username.place(x=50, y=400, width=250, height=35)
        
        #password Label
        password_lbl = Label(frame, text="Password:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        password_lbl.place(x=450, y=370)
        self.txt_password = Entry(frame,textvariable=self.var_password , font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=450, y=400, width=250, height=35)
        
        #confirm password Label
        cpassword_lbl = Label(frame, text="Confirm Password:", font=("times new roman", 15, "bold"), fg="gray", bg="white")
        cpassword_lbl.place(x=50, y=450)
        self.txt_cpassword = Entry(frame,textvariable=self.var_cpassword , font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=50, y=480, width=250, height=35)
        
        #check button
        self.var_chk = IntVar()
        check_btn = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        check_btn.place(x=50, y=520)
        
        #register button
        img = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\register.png")
        img = img.resize((100, 50),Image.Resampling.LANCZOS )
        self.photoimg = ImageTk.PhotoImage(img)
        register_btn = Button(frame,command=self.register_data, image=self.photoimg, bd=0, cursor="hand2")
        register_btn.place(x=300, y=550)
        
        #function declaration
    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_lname.get() == "" or self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_username.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
                messagebox.showerror("Error", "Password and Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
                messagebox.showerror("Error", "Please Agree to the Terms & Conditions", parent=self.root)
        else:
                conn = mysql.connector.connect(host="localhost", user="root", password="Sahil&@80085", database="new_users")
                cur = conn.cursor()
                query = ("SELECT * FROM register where email=%s")
                values = (self.txt_email.get(),)
                cur.execute(query, values)
                row = cur.fetchone()
                if row != None:
                        messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                        cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.txt_fname.get(), 
                                self.txt_lname.get(), 
                                self.txt_contact.get(), 
                                self.txt_email.get(), 
                                self.var_securityQ.get(), 
                                self.txt_answer.get(), 
                                self.txt_username.get(), 
                                self.txt_password.get()
                                ))
                        conn.commit()
                        conn.close() 
                        messagebox.showinfo("Success", "Registration Successful",parent=self.root)
    
       


if __name__ == "__main__":
    root = Tk()
    app =Register(root)
    root.mainloop()