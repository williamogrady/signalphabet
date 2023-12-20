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

        b = tk.Button(self.log_frame, text = "1", bg = "red")
        b.grid(row=1, column=3)
        b2 =tk.Button(self.log_frame, text = "2")
        b2.grid(row=1, column=4)
        b3 = tk.Button(self.log_frame, text = "2")
        b3.grid(row=2, column=0)

        
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
