import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("1200x900")


# NY CLASS #
class Camera():
    label_widget = tk.Label(app) # Create a label and display it on app 
    label_widget.grid(row=0, column=0) 
  
    def open_camera(): 
        # Capture the video frame by frame 
        _, frame = vid.read() 
    
        # Convert image from one color space to other 
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image) 
    
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
    
        # Displaying photoimage in the label 
        label_widget.photo_image = photo_image 
    
        # Configure image in the label 
        label_widget.configure(image=photo_image) 
    
        # Repeat the same process after every 10 seconds 
        label_widget.after(10, open_camera) 
    
  
# Show cam
open_camera()

text = tk.Label(app, text="Do this")
text.grid(row=0, column=1)

image = Image.open("interface/testpicture.png").resize((400, 400))
bing = ImageTk.PhotoImage(image)

label = ttk.Label(app, image=bing)
label.grid(row=1, column=1)
        

vid = cv2.VideoCapture(0)
vid

app.mainloop()