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
        self.frame1.grid_rowconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(0, weight=5)  # Left column
        self.frame1.grid_columnconfigure(1, weight=1)  # Middle column
        self.frame1.grid_columnconfigure(2, weight=4)  # Right column

        self.create_left_grid()

        self.label_widget = Label(self.frame1)
        self.label_widget.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")  # Camera in the right column

        self.vid = cv2.VideoCapture(0)
        self.show_frame()

        self.frame1.pack(expand=True, fill="both")

    def create_left_grid(self):
        for i in range(3):
            self.frame1.grid_rowconfigure(i, weight=1)
            for j in range(5):
                frame_color = "red" if (i + j) % 2 == 0 else None
                frame = Frame(self.frame1, bg=frame_color)
                frame.grid(row=i, column=j, sticky="nsew")
                frame.grid_columnconfigure(0, weight=1)

    def show_frame(self):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.label_widget.imgtk = imgtk
            self.label_widget.config(image=imgtk)

            self.label_widget.after(10, self.show_frame)
        else:
            print("Failed to capture frame.")

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
