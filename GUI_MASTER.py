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
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
root = tk.Tk()
root.title("Student Academic Success Prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image = Image.open('img3.jpg')

image = image.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
# function to change to next image
'''def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img3)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()'''




  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Machine Learning Based Predicting Student Academic Success", font=('times', 35,' bold '), height=2, width=62,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    data = pd.read_csv("D:/project/Student_performance/Student_performance/Student_performance/ab (1).csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

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
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=305,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as student_performance.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=305,y=420)
    from joblib import dump
    dump (svcclassifier,"student_performance.joblib")
    print("Model saved as student_performance.joblib")



def call_file():
    from subprocess import call
    call(['python','Check.py'])
    #import Check.py
    #Check.py()




def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=5, y=200)

button4 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Check Performance", command=call_file, width=15, height=2)
button4.place(x=5, y=280)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=380)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''