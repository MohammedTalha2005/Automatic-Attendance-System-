import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
import mysql.connector
from datetime import datetime

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"


class FaceRecognitionApp:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_label = ctk.CTkLabel(self.root, text="FACE RECOGNITION", 
                                   font=ctk.CTkFont(size=35, weight="bold"), 
                                   text_color="green")
        title_label.place(x=0, y=0, width=1400, height=45)

        # Top Image
        img_top = Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\WhatsApp Image 2025-02-06 at 02.25.52_0c6c591e.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        top_img_label = ctk.CTkLabel(self.root, image=self.photoimg_top, text="")
        top_img_label.place(x=0, y=50, width=650, height=700)

        # Bottom Image
        img_bottom = img_top.copy()  # Using the same image for simplicity
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bottom_img_label = ctk.CTkLabel(self.root, image=self.photoimg_bottom, text="")
        bottom_img_label.place(x=650, y=50, width=750, height=700)

        # Buttons
        face_recog_button = ctk.CTkButton(bottom_img_label, text="Live Face Recognition", 
                                          font=ctk.CTkFont(size=16, weight="bold"),
                                          fg_color="#A7E1E9", text_color="black", 
                                          corner_radius=25, command=self.live_face_recognition)
        face_recog_button.place(x=200, y=600, width=180, height=40)

        upload_image_button = ctk.CTkButton(bottom_img_label, text="Upload Image", 
                                            font=ctk.CTkFont(size=16, weight="bold"),
                                            fg_color="#FFA500", text_color="black", 
                                            corner_radius=25, command=self.upload_and_recognize)
        upload_image_button.place(x=400, y=600, width=180, height=40)

    # Function to recognize face from an uploaded image
    def upload_and_recognize(self):
        file_path = filedialog.askopenfilename(title="Select an Image", 
                                               filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
        if not file_path:
            messagebox.showerror("Error", "No image selected!", parent=self.root)
            return

        uploaded_img = cv2.imread(file_path)
        if uploaded_img is None:
            messagebox.showerror("Error", "Invalid image file!", parent=self.root)
            return

        self.recognize_face_from_image(uploaded_img)

    def recognize_face_from_image(self, img):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)

        for (x, y, w, h) in faces:
            id, predict = clf.predict(gray[y:y+h, x:x+w])
            confidence = int(100 * (1 - predict / 300))

            conn = mysql.connector.connect(host="localhost", username="root", password="Sahil&@80085", database="face_recognizer")
            cursor = conn.cursor()
            cursor.execute("SELECT Name, roll, department FROM student WHERE Student_id=%s", (id,))
            result = cursor.fetchone()
            conn.close()

            if result and confidence > 77:
                name, roll, department = result
                cv2.putText(img, f"ID: {id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(img, f"Roll: {roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(img, f"Name: {name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(img, f"Department: {department}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
            else:
                cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

        cv2.imshow("Face Recognition", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Function for live face recognition
    def live_face_recognition(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = self.recognize_live_face(img, clf, face_cascade)
            cv2.imshow("Live Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def recognize_live_face(self, img, clf, face_cascade):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)

        for (x, y, w, h) in faces:
            id, predict = clf.predict(gray[y:y+h, x:x+w])
            confidence = int(100 * (1 - predict / 300))

            if confidence > 77:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(img, f"ID: {id}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
            else:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(img, "Unknown", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

        return img


if __name__ == "_main_":
    root = ctk.CTk()
    app = FaceRecognitionApp(root)
    root.mainloop()