import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self) 
        self.geometry("1200x900")
        self.container.pack(side = "top", fill = "both", expand = True) 

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1) 
        self.container.grid_columnconfigure(1, weight = 1)

        # Test code #
        red = tk.Frame(self.container, background="red")
        red.grid(column = 1, sticky = "news")
        # # # # # # #

        self.frames = {} 
        
        for F in (StartPage, AlphabetPage, GamePage):
            frame = F(self.container, self)
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")        
        self.show_frame(StartPage)


        #cameraframe = Camera(self, container)
        #cameraframe.grid(row = 0, column = 1, sticky ="nsew")     
        #self.show_camera(Camera)
          


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #def show_camera(self, cont):
        #cameraframe = self.frames[cont]
        #cameraframe.tkraise()
  

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Start", font = ("Arial", 14))
        label.pack()
        
        bluebutton = ttk.Button(self, text ="Alphabet", command = lambda : controller.show_frame(AlphabetPage))
        bluebutton.pack()



class AlphabetPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Alphabet", font = ("Arial", 14))
        label.pack()
        
        redbutton = ttk.Button(self, text ="Game", command = lambda : controller.show_frame(GamePage))
        redbutton.pack()


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Game", font = ("Arial", 14))
        label.pack()
       
        greenbutton = ttk.Button(self, text ="Green", command = lambda : controller.show_frame(StartPage))
        greenbutton.pack()

# NY CLASS #
        """
class Camera(tk.Frame):
    def __init__(self, parent):
        vid = cv2.VideoCapture(0).__init__(self, parent)
        label_widget = tk.CTkLabel(app) # Create a label and display it on app 
        label_widget.grid(row=0, column=0) 

        def open_camera(): 
            _, frame = vid.read() 
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
            captured_image = Image.fromarray(opencv_image) 
            photo_image = ImageTk.PhotoImage(image=captured_image) 
            label_widget.photo_image = photo_image 
            label_widget.configure(image=photo_image) 
            label_widget.after(10, open_camera) 
        
        open_camera() 
"""

# Create a function to open camera and 
# display it in the label_widget on app 
  
app = tkinterApp()

vid = cv2.VideoCapture(0) # Define a video capture object 

"""
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
    app.container.photo_image = photo_image 
  
    # Configure image in the label 
    app.container.configure(image=photo_image) 
  
    # Repeat the same process after every 10 seconds 
    app.container.after(10, open_camera) 

open_camera()

"""
app.mainloop()