from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl = Label(self.root, text="TRAIN DATA", font=("Helvetica", 35, "bold"), bg="white", fg="RED")
        title_lbl.place(x=0, y=0, width=1365, height=45)

        img_top= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\bg-image.jpg")
        img_top= img_top.resize((1365, 300), Image.Resampling.LANCZOS)
        self.photoimg_top= ImageTk.PhotoImage(img_top) 
        
        f_lbl = Label(self.root, image=self.photoimg_top) #RESIZE IMAGE
        f_lbl.place(x=0, y=50, width=1365, height=300)

        #button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2", font=("Helvetica", 30, "bold"), bg="BLUE", fg="white")
        b1_1.place(x=0, y=350, width=1365, height=60)

        img_bottom= Image.open(r"C:\Users\win10\OneDrive\Desktop\Face Recognition System\public\assets\images\bg-image.jpg")
        img_bottom= img_bottom.resize((1365, 300), Image.Resampling.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom) 
        
        f_lbl = Label(self.root, image=self.photoimg_bottom) #RESIZE IMAGE
        f_lbl.place(x=0, y=410, width=1365, height=300)

        
    def train_classifier(self) :
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #===============Train the classefier and save=============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")













                
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
