from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_qwe import Face_Recognition
from attendance import Attendance

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x720+0+0")
        self.root.title("Face Recognition System")
        # First Image
        img = Image.open(r"D:\Projects\Attendence System\AI-Attendance-main\AI-Attendance-main\images\AppleHealthy.jpg")
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
        bg_img.place(x=0, y=130, width=1540, height=720)
        
        #Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1540, height=45)
        
        #student button-1
        img4 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\icons8-register-100.png")
        img4 = img4.resize((120,120), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4) 
        bt1_photo = Label(bg_img, image=self.photoimg4)
        bt1_photo.place(x=200, y=100, width=200, height=200)
        b1_1 = Button(bg_img, text="Register A Student",command = self.student_details , cursor="hand2", font=("Helvetica", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=200, y=300, width=200, height=40)

         #student button-2
        img5 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\facial_recog.png")
        img5 = img5.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        bt2_photo = Label(bg_img, image=self.photoimg5)
        bt2_photo.place(x=600, y=100, width=200, height=200)
        b2_1 = Button(bg_img,command=self.face_rec_window, text="Face Detector", cursor="hand2", font=("Helvetica", 15, "bold"), bg="green", fg="white")
        b2_1.place(x=600, y=300, width=200, height=40)
        
        
        #student button-3
        img6 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\images.png")
        img6 = img6.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        bt3_photo = Label(bg_img, image=self.photoimg6)
        bt3_photo.place(x=1000, y=100, width=200, height=200)
        b3_1 = Button(bg_img,command=self.train_window, text="Train Model", cursor="hand2", font=("Helvetica", 15, "bold"), bg="green", fg="white")
        b3_1.place(x=1000, y=300, width=200, height=40)
        
        # button - 4 
        img7 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\download.png")
        img7 = img7.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7) 
        bt4_photo = Label(bg_img, image=self.photoimg7)
        bt4_photo.place(x=200, y=400, width=200, height=200)
        b4_1 = Button(bg_img,command=self.attendance_window, text="Attendence", cursor="hand2", font=("Helvetica", 15, "bold"), bg="green", fg="white")
        b4_1.place(x=200, y=600, width=200, height=40)
        
        # button - 5 
        img8 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\download (1).png")
        img8= img8.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8) 
        bt4_photo = Label(bg_img, image=self.photoimg8)
        bt4_photo.place(x=600, y=400, width=200, height=200)
        b4_1 = Button(bg_img, text="Chat Bot", cursor="hand2", font=("Helvetica", 15, "bold"), bg="green", fg="white")
        b4_1.place(x=600, y=600, width=200, height=40)
        
        # button - 6
        img9 = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\icons8-login-100.png")
        img9= img9.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg9= ImageTk.PhotoImage(img9) 
        bt4_photo = Label(bg_img, image=self.photoimg9)
        bt4_photo.place(x=1000, y=400, width=200, height=200)
        b4_1 = Button(bg_img, text="Exit", cursor="hand2", font=("Helvetica", 15, "bold"), bg="green", fg="white")
        b4_1.place(x=1000, y=600, width=200, height=40)
        
        # button Functions
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    def  train_window(self):
         self.new_window = Toplevel(self.root)
         self.app = Train(self.new_window)
    def  attendance_window(self):
         self.new_window = Toplevel(self.root)
         self.app =Attendance(self.new_window)
    def  face_rec_window(self):
         self.new_window = Toplevel(self.root)
         self.app = Face_Recognition(self.new_window)
    
         
    

        
        
# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
