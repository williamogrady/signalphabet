import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk

## APPLICATION CLASS ##

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Sign Alphabet")

## INIT INTERFACE ##
        
        self.camera_page()
        self.start_camera()

        self.start_page()


## CAMERA STUFF ##

    def camera_page(self):

        # Create a frame for the camera recording area
        self.camera_frame = tk.Frame(self, width=640, height=480)
        self.camera_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a label to display the camera feed
        self.camera_label = tk.Label(self.camera_frame)
        self.camera_label.pack()

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


## INTERFACE PAGES ##

    def start_page(self):        
        # Start Page
         
        self.start_page_frame = tk.Frame(self, width=200, height=480)
        self.start_page_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        b = tk.Button(self.start_page_frame, text = "1", bg = "red", command=self.alphabet_page)
        b.grid(row=1, column=3)
        b2 =tk.Button(self.start_page_frame, text = "2")
        b2.grid(row=1, column=4)
        b3 = tk.Button(self.start_page_frame, text = "2")
        b3.grid(row=2, column=0)

        
    def alphabet_page(self):
        #Alphabet Page

        self.alpha_page_frame = tk.Frame(self, width=200, height=480)
        self.alpha_page_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        b = tk.Button(self.start_page_frame, text = "1", bg = "blue", command=self.start_page)
        b.grid(row=1, column=3)
        b2 =tk.Button(self.start_page_frame, text = "2")
        b2.grid(row=1, column=4)
        b3 = tk.Button(self.start_page_frame, text = "2")
        b3.grid(row=2, column=0)




# Create an instance of the application
app = Application()
app.resizable(False,False)

# Start the main event loop
app.mainloop()


"""
class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x900")
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.pack()
        self.register_btn = ttk.Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.pack()
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

root = Tk()
app(root)
root.mainloop()

"""