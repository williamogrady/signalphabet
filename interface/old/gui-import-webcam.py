import tkinter as tk
from tkinter import ttk
import cv2 
from PIL import Image, ImageTk 


img = cv2.imread("a-sign.png", cv2.IMREAD_ANYCOLOR)
  
vid = cv2.VideoCapture(0) # Define a video capture object 

  
width, height = 800, 600 # Declare the width and height in variables 
  
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 
  

app = tk.Tk() # Create a GUI app 
app.geometry("1200x800")

app.bind('<Escape>', lambda e: app.quit())  # Bind the app with Escape keyboard to quit app whenever pressed 

app.grid_columnconfigure(0, weight = 1)
app.grid_columnconfigure(1, weight = 1)
app.grid_rowconfigure(0, weight = 1)
app.grid_rowconfigure(1, weight = 1)




#rightframe = tk.CTkFrame(app)

#rightframe.grid_columnconfigure(0, weight = 1)
#rightframe.grid_rowconfigure(0, weight = 1)
#rightframe.grid_rowconfigure(1, weight = 1)


label_widget = tk.Label(app) # Create a label and display it on app 
label_widget.grid(row=0, column=0) 
  
# Create a function to open camera and 
# display it in the label_widget on app 
  
  
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


#picture= tk.CTkImage(app, light_image = img)
#picture.grid(row=0, column=1)
  
# Create an infinite loop for displaying app on screen 
app.mainloop() 
