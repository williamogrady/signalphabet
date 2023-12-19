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
        self.frame1.grid_columnconfigure(0, weight=7)
        self.frame1.grid_columnconfigure(1, weight=1)

        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.grid(row=0, column=0, sticky="w", pady=10)

        self.practice_btn = ttk.Button(self.frame1, text="Go to Alphabet Page", command=self.alphabet_page)
        self.practice_btn.grid(row=1, column=0, sticky="w", pady=10)

        self.label_widget = Label(self.frame1)
        self.label_widget.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.vid = cv2.VideoCapture(0)
        self.show_frame()

        self.frame1.pack(expand=True, fill="both")

    def show_frame(self):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get the dimensions of the label widget
            label_width = self.label_widget.winfo_width()
            label_height = self.label_widget.winfo_height()

            # Crop and resize the frame to fill the label widget
            frame = self.crop_and_resize(frame, label_width, label_height)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.label_widget.imgtk = imgtk
            self.label_widget.config(image=imgtk)

            self.label_widget.after(10, self.show_frame)
        else:
            print("Failed to capture frame.")

    def crop_and_resize(self, frame, target_width, target_height):
        height, width, _ = frame.shape

        # Calculate the center of the frame
        center_x, center_y = width // 2, height // 2

        # Calculate the cropping box
        x1 = max(center_x - target_width // 2, 0)
        y1 = max(center_y - target_height // 2, 0)
        x2 = min(center_x + target_width // 2, width)
        y2 = min(center_y + target_height // 2, height)

        # Ensure the cropping box is valid
        if x1 < x2 and y1 < y2:
            # Crop the frame
            cropped_frame = frame[y1:y2, x1:x2]

            # Resize the frame to the target dimensions
            resized_frame = cv2.resize(cropped_frame, (target_width, target_height))

            return resized_frame
        else:
            # Return an empty black frame if the cropping box is invalid
            return np.zeros((target_height, target_width, 3), dtype=np.uint8)

    def alphabet_page(self):
        # Add functionality for transitioning to the alphabet page
        pass

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()