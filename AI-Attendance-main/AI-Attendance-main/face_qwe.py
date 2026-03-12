from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import tkinter as tk
import customtkinter as ctk
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        img_top= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\WhatsApp Image 2025-02-06 at 02.25.52_0c6c591e.jpg")
        img_top= img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top= ImageTk.PhotoImage(img_top) 
        
        f_lbl = Label(self.root, image=self.photoimg_top) 
        f_lbl.place(x=0, y=50, width=650, height=700)

        img_bottom= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\WhatsApp Image 2025-02-06 at 02.25.52_0c6c591e.jpg")
        img_bottom= img_bottom.resize((750, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom) 
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=50, width=750, height=700)

        # **Face Recognition Button**
        b1_1 = ctk.CTkButton(f_lbl, text="Live Face Recognition",
                            font=("Century Gothic", 16, "bold"),
                            fg_color="#A7E1E9",
                            text_color="black",
                            hover_color="#8FD1D9",
                            corner_radius=25,
                            width=80, height=40,
                            cursor="hand2",
                            border_width=0,
                            bg_color="#384c60",
                            command=self.face_recog)

        b1_1.place(x=200, y=600)

        # **Upload Image Button**
        upload_btn = ctk.CTkButton(f_lbl, text="Upload Image",
                            font=("Century Gothic", 16, "bold"),
                            fg_color="#FFA500",
                            text_color="black",
                            hover_color="#FF8C00",
                            corner_radius=25,
                            width=100, height=40,
                            cursor="hand2",
                            border_width=0,
                            bg_color="#384c60",
                            command=self.upload_and_recognize)

        upload_btn.place(x=400, y=600)


    # **Function to Recognize from Uploaded Image**
    def upload_and_recognize(self):
        file_path = filedialog.askopenfilename(title="Select an Image",
                                               filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        if not file_path:
            messagebox.showerror("Error", "No image selected!", parent=self.root)
            return

        # Load the image and process it
        uploaded_img = cv2.imread(file_path)
        if uploaded_img is None:
            messagebox.showerror("Error", "Invalid image file!", parent=self.root)
            return

        self.recognize_face_from_image(uploaded_img)


    # **Face Recognition from an Image**
    def recognize_face_from_image(self, img):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # Load trained model

        processed_img = self.recognize(img, clf, faceCascade)
        cv2.imshow("Uploaded Image Recognition", processed_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    # **Live Face Recognition**
    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  # Load trained model

        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Live Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


    # **Face Detection & Recognition**
    def recognize(self, img, clf, faceCascade):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 10)

        for (x, y, w, h) in faces:
            id, predict = clf.predict(gray[y:y+h, x:x+w])
            confidence = int((100 * (1 - predict / 300)))

            # **Search for the recognized ID in the Data Folder**
            data_path = "data/"
            matched_image = None
            for filename in os.listdir(data_path):
                if filename.startswith(str(id)):  # Match ID with stored images
                    matched_image = os.path.join(data_path, filename)
                    break

            conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
            n = my_cursor.fetchone()
            n = "+".join(n) if n else "Unknown"

            my_cursor.execute("SELECT roll FROM student WHERE Student_id=" + str(id))
            r = my_cursor.fetchone()
            r = "+".join(r) if r else "Unknown"

            my_cursor.execute("SELECT department FROM student WHERE Student_id=" + str(id))
            d = my_cursor.fetchone()
            d = "+".join(d) if d else "Unknown"

            if confidence > 77:
                cv2.putText(img, f"ID: {id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                cv2.putText(img, f"Roll: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8,  (0, 0, 255), 3)
                cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,  (0, 0, 255), 3)
                self.mark_attendance(id, r, n, d)
            else:
                cv2.rectangle(img, (x, y), (x+w, y+h),   (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,  (0, 0, 255), 3)

        return img


    # **Mark Attendance**
    def mark_attendance(self, i, r, n, d):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
