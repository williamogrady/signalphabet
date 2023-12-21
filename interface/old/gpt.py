from tkinter import *
from tkinter import ttk
import cv2
import numpy as np
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x900")
        self.start_page()

    def start_page(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame1 = Frame(self.master)
        self.frame1.grid_rowconfigure(0, weight=1)  # First/top Row
        self.frame1.grid_rowconfigure(1, weight=2)
        self.frame1.grid_rowconfigure(2, weight=4)
        self.frame1.grid_rowconfigure(3, weight=1)  # Bottom row

        self.frame1.grid_columnconfigure(0, weight=1)  # Left column
        self.frame1.grid_columnconfigure(1, weight=3)  # Left middle column
        self.frame1.grid_columnconfigure(2, weight=1)  # Right middle column
        self.frame1.grid_columnconfigure(3, weight=5)  # Right column

        frame_text_left = Frame(self.frame1, bg="red")
        frame_text_middle = Frame(self.frame1, bg="yellow")
        frame_text_right = Frame(self.frame1, bg="blue")
        frame_text_explanations = Frame(self.frame1, bg="purple")
        frame_picture = Frame(self.frame1, bg="lightblue")
        frame_text_bottom_right = Frame(self.frame1, bg="black")

        frame_text_left.grid(row=0, column=1, sticky="news")
        frame_text_middle.grid(row=0, column=2, sticky="news")
        frame_text_right.grid(row=0, column=3, sticky="news")
        frame_text_explanations.grid(row=1, column=2, sticky="news")
        frame_picture.grid(row=2, column=2, sticky="news")
        frame_text_bottom_right.grid(row=3, column=2, sticky="news")

        # Button to open the camera window
        open_camera_btn = ttk.Button(frame_text_middle, text="Open Camera", command=self.open_camera_window)
        open_camera_btn.pack(pady=10)

        self.frame1.pack(expand=True, fill="both")

    def open_camera_window(self):
        camera_window = Toplevel(self.master)
        camera_app = CameraApp(camera_window)

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.camera_frame()

    def camera_frame(self):
        for i in self.master.winfo_children():
            i.destroy()

        label_widget = Label(self.master)
        label_widget.pack(expand=True, fill="both")

        vid = cv2.VideoCapture(0)
        self.show_frame(label_widget, vid)

    def show_frame(self, label_widget, vid):
        ret, frame = vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            label_widget.imgtk = imgtk
            label_widget.config(image=imgtk)

            label_widget.after(10, lambda: self.show_frame(label_widget, vid))
        else:
            print("Failed to capture frame.")

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
