import tkinter as tk  #GUI
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk  #image manipulation
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2  # openCV used for image processing
import sqlite3  #database
import os
import numpy as np #mathematical operations
import time
from tkvideo import tkvideo
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Machine Learning Based Predicting Student Academic Success")

# 43
video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("studentvideo.mp4", video_label,loop = 1, size = (w, h))
player.play()


label_l1 = tk.Label(root, text="Predicting Student Academic Success",font=("Times New Roman", 35, 'bold'),
                    background="dark blue", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)



def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","log.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=12, height=1,font=('times', 20, ' bold '), bg="dark blue", fg="white")
button1.place(x=80, y=160)

button2 = tk.Button(root, text="Register",command=reg,width=12, height=1,font=('times', 20, ' bold '), bg="dark blue", fg="white")
button2.place(x=80, y=260)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=80, y=360)

root.mainloop()