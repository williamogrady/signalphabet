import tkinter as tk
import cv2
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Sign Alphabet")
        
        # Create a frame for the camera recording area
        self.camera_frame = tk.Frame(self, width=640, height=480)
        self.camera_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Create a frame for the notification log
        self.log_frame = tk.Frame(self, width=200, height=480)
        self.log_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.log_frame2 = tk.Frame(self, width=200, height=480)
        self.log_frame2.pack(side=tk.RIGHT, padx=10, pady=10)

        button =tk.Button(self.log_frame, text = "Gridddd")
        button.pack()

        button2 = tk.Button(self.log_frame2, text ="Testest")
        button2.grid(row=1,column=1)

        
        # Create a label to display the camera feed
        self.camera_label = tk.Label(self.camera_frame)
        self.camera_label.pack()
        
        # Create a text widget for the notification log
        
        # Start the camera feed
        self.start_camera()
        
    def start_camera(self):
        # Open the camera
        self.cap = cv2.VideoCapture(0)
        
        # Update the camera feed every 10 milliseconds
        self.update_camera()
        
    def update_camera(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()
        
        if ret:
            # Convert the frame to PIL format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            
            # Resize the image to fit the label
            image = image.resize((640, 480))
            
            # Convert the image to Tkinter format
            photo = ImageTk.PhotoImage(image)
            
            # Update the label with the new image
            self.camera_label.configure(image=photo)
            self.camera_label.image = photo
        
        # Schedule the next update
        self.after(10, self.update_camera)
        
    def log_notification(self, notification):
        # Append the notification to the log
        self.log_text.insert(tk.END, notification + "\n")
        
        # Scroll to the bottom of the log
        self.log_text.see(tk.END)

# Create an instance of the application
app = Application()
app.resizable(False,False)

# Start the main event loop
app.mainloop()





"""
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
"""