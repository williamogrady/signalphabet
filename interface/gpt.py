from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import numpy as np

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
        self.frame1.grid_columnconfigure(0, weight=5)
        self.frame1.grid_columnconfigure(1, weight=1)
        self.frame1.grid_columnconfigure(2, weight=3)
        self.frame1.grid_columnconfigure(3, weight=1)

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

        self.vid = cv2.VideoCapture(0)
        self.show_frame(frame_picture)

        self.frame1.pack(expand=True, fill="both")

    def show_frame(self, frame_widget):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Get the dimensions of the frame widget
            frame_width = frame_widget.winfo_width()
            frame_height = frame_widget.winfo_height()

            # Adjust the target dimensions to fit the frame widget
            target_width = frame_width
            target_height = frame_width * frame.shape[0] // frame.shape[1]

            # Crop and resize the frame to fill the frame widget
            frame = self.crop_and_resize(frame, target_width, target_height)

            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            label_widget = Label(frame_widget, image=imgtk)
            label_widget.imgtk = imgtk
            label_widget.config(image=imgtk)
            label_widget.pack(fill="both", expand=True)

            label_widget.after(10, lambda: self.show_frame(frame_widget))
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
            # If the cropping box is invalid, resize the entire frame to the target dimensions
            resized_frame = cv2.resize(frame, (max(target_width, 1), max(target_height, 1)))
            return resized_frame


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
