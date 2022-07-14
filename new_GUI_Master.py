import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Student Performance Prediction System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img3.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Predicting Student Academic Success",font=("Times New Roman", 35, 'bold'),
                    background="dark blue", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


def reg():
    
    data = pd.read_csv("D:/project/Student_performance/Student_performance/Student_performance/ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""
    #Done to increase efficiency

    le = LabelEncoder()
    data['gender'] = le.fit_transform(data['gender'])
    data['Nationlity'] = le.fit_transform(data['Nationlity'])
    data['PlaceofBirth'] = le.fit_transform(data['PlaceofBirth'])
    data['StageID'] = le.fit_transform(data['StageID'])
    data['GradeID'] = le.fit_transform(data['GradeID'])
    data['Topic'] = le.fit_transform(data['Topic'])
    data['Semester'] = le.fit_transform(data['Semester'])
    data['VisitedResources'] = le.fit_transform(data['VisitedResources'])
    data['AnnouncementsView'] = le.fit_transform(data['AnnouncementsView'])
    data['Discussion'] = le.fit_transform(data['Discussion'])
    data['ParentAnsweringSurvey'] = le.fit_transform(data['ParentAnsweringSurvey'])
    data['ParentsShoolSatisfaction'] = le.fit_transform(data['ParentsShoolSatisfaction'])
    data['StudentAbsenceDays'] = le.fit_transform(data['StudentAbsenceDays'])
   
       

    """Feature Selection => Manual"""
    x = data.drop(['Relation','raisedhands','SectionID','Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='light blue',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=370,y=180)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as student_performance.joblib",width=45,height=3,bg='orange',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=370,y=400)
    from joblib import dump
    dump (svcclassifier,"student_performance.joblib")
    print("Model saved as student_performance.joblib")




def log():
    from subprocess import call
    call(["python","Check.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Model Training", command=reg, width=12, height=1,font=('times', 20, ' bold '), bg="dark blue", fg="white")
button1.place(x=80, y=160)

button2 = tk.Button(root, text="Check Performance",command=log,width=14, height=1,font=('times', 20, ' bold '), bg="dark blue", fg="white")
button2.place(x=80, y=250)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="black")
button3.place(x=80, y=360)

root.mainloop()