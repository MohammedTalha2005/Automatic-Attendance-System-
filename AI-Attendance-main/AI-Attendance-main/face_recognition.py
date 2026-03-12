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


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       
       
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1365, height=45)

        img_top= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\WhatsApp Image 2025-02-06 at 02.25.52_0c6c591e.jpg")
        img_top= img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top= ImageTk.PhotoImage(img_top) 
        
        f_lbl = Label(self.root, image=self.photoimg_top) #RESIZE IMAGE
        f_lbl.place(x=0, y=50, width=650, height=700)

        img_bottom= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\WhatsApp Image 2025-02-06 at 02.25.52_0c6c591e.jpg")
        img_bottom= img_bottom.resize((750, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom) 
        
        f_lbl = Label(self.root, image=self.photoimg_bottom) #RESIZE IMAGE
        f_lbl.place(x=650, y=50, width=750, height=700)

         #button
        
       # b1_1 = Button(f_lbl, text="Face Recognition",cursor="hand2", font=("Century Gothic", 16, "bold"), bg="#A7E1E9", bd=4, relief="ridge", fg="white")
       # b1_1.place(x=290, y=600, width=200, height=40)
        b1_1 = ctk.CTkButton(f_lbl,command=self.face_recog ,text="Face Recognition",
                            font=("Century Gothic", 16, "bold"),
                            fg_color="#A7E1E9",  # Button background color
                            text_color="black",  # Text color
                            hover_color="#8FD1D9",  # Hover effect
                            corner_radius=25,  # Rounded corners
                            width=200, height=40,
                            cursor="hand2",
                            border_width=0,  # Remove border
                            bg_color="#384c60")  # Set to transparent

        b1_1.place(x=290, y=600)

    #==========Attendance==============

    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #==========face recognition========

    # def face_recog(self):
    #     def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
    #         gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #         features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

    #         coord=[]

    #         for(x,y,w,h) in features:
    #             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    #             id,predict=clf.predict(gray_image[y:y+h,x:x+w])
    #             confidence=int((100*(1-predict/300)))
                
    #             conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
    #             my_cursor=conn.cursor()
               
    #             my_cursor.execute("Select Name from Student where Student_ID="+str(id))
    #             n=my_cursor.fetchone()
    #             n="+".join(n)

    #             my_cursor.execute("Select Roll from Student where Student_ID="+str(id))
    #             r=my_cursor.fetchone()
    #             r="+".join(r)

    #             my_cursor.execute("Select Dep from Student where Student_ID="+str(id))
    #             d=my_cursor.fetchone()
    #             d="+".join(d)
               
    #             my_cursor.execute("Select Student ID from Student where Student_ID="+str(id))
    #             i=my_cursor.fetchone()
    #             i="+".join(d)
            


    #             if confidence>77:
    #                 cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
    #                 self.mark_attendance(i,r,n,d)
    #             else:
    #                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    #                 cv2.putText(img,f"Unknown Face:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

    #             coord=[x,y,w,y]

    #         return coord
        
    #     def recognize(img,clf,faceCascade):
    #         coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
    #         return img

    #     faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #     clf=cv2.face.LBPHFaceRecognizer_create()
    #     clf.read("classifier.xml")

    #     video_cap=cv2.VideoCapture(0)
        
    #     while True:
    #         ret,img=video_cap.read()
    #         img=recognize(img,clf,faceCascade)
    #         cv2.imshow("Welcome To Face Recognition",img)

    #         if cv2.waitKey(1)==13:
    #             break
    #         video_cap.release()
    #         cv2.destroyAllWindows()
    def face_recog(self):
            def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                # Convert to grayscale
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
                coord = []
                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int(100 * (1 - predict/300))
                    
                    conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("SELECT Name FROM Student WHERE Student_ID=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n else "Unknown"
            
                    my_cursor.execute("SELECT Roll FROM Student WHERE Student_ID=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r else "Unknown"
            
                    my_cursor.execute("SELECT Dep FROM Student WHERE Student_ID=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d) if d else "Unknown"
            
                    # Notice: Correcting column name if necessary. Here, I assume it's Student_ID.
                    my_cursor.execute("SELECT Student_ID FROM Student WHERE Student_ID=" + str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i) if i else "Unknown"
            
                    conn.close()
                    
                    if confidence > 77:
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    coord = [x, y, w, h]  # corrected coordinate list
                return coord
            
            def recognize(img, clf, faceCascade):
                coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
                return img

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)
            
            while True:
                ret, img = video_cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)
                if cv2.waitKey(1) == 13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()