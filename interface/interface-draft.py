import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk 

class tkinterApp(tk.Tk):
    
  
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        self.geometry("1200x900")
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)


        self.frames = {} 

 
        for F in (StartPage, AlphabetPage):

            frame = F(container, self)  

            self.frames[F] = frame 

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    """  
    def open_camera(self, vid, widget):
        _, frame = vid.read() 
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
        captured_image = Image.fromarray(opencv_image) 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
        widget.photo_image = photo_image 
        widget.configure(image=photo_image) 
        widget.after(10, self.open_camera) 
        """ 

class StartPage(tkinterApp, tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        self.columnconfigure(0, weight = 5)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 5)
        self.columnconfigure(3, weight = 1)
        
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 2)
        self.rowconfigure(2, weight = 4)
        self.rowconfigure(3, weight = 1)
        
        frame_text_left = tk.Frame(self, bg="red")
        frame_text_middle = tk.Frame(self, bg="red")
        frame_text_right = tk.Frame(self, bg="red")
        frame_text_explenations = tk.Frame(self, bg="red")
        frame_picture = tk.Frame(self, bg="red")
        frame_text_bottom_right = tk.Frame(self, bg="red")
    
        frame_text_left.grid(row=0, column=1,sticky = "news")
        frame_text_middle.grid(row=0, column=2, sticky="news")
        frame_text_right.grid(row=0, column=3, sticky="news")
        frame_text_explenations.grid(row=1, column=2, sticky="news")
        frame_picture.grid(row=2, column=2, sticky="news")
        frame_text_bottom_right.grid(row=3, column=2, sticky="news")
        bluebutton = ttk.Button(self, text ="Blue", command = lambda : controller.show_frame(AlphabetPage))
        bluebutton.grid(row=3, column=2, sticky="news")
        
        #vid = cv2.VideoCapture(0)
        #label_widget = tk.Label(self)
        #label_widget.grid(row=0, column=0) 

        #tkinterApp.open_camera(self, vid, label_widget)


class AlphabetPage(tkinterApp, tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
    

app = tkinterApp()
app.mainloop()