import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("1200x900")


# NY CLASS #
class Camera():
    def __init__(self):
        label_widget = tk.Label(app) # Create a label and display it on app 
        label_widget.grid(row=0, column=0) 
        
  
    def open_camera(self, vid, label_widget):      
        _, frame = vid.read()
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
        captured_image = Image.fromarray(opencv_image) 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
        label_widget.photo_image = photo_image 
        label_widget.configure(image=photo_image) 
        label_widget.after(10, self.open_camera) 
        

vid = cv2.VideoCapture(0)
cameraframe = Camera()
cameraframe.open_camera(vid,app)

app.mainloop()