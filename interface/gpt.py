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
        self.frame1.grid_columnconfigure(0, weight=4)
        self.frame1.grid_columnconfigure(1, weight=4)

        self.create_left_grid()

        self.label_widget = Label(self.frame1)
        self.label_widget.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

        self.vid = cv2.VideoCapture(0)
        self.show_frame()

        self.frame1.pack(expand=True, fill="both")

    def create_left_grid(self):
        for i in range(3):
            self.frame1.grid_rowconfigure(i, weight=1)
            for j in range(3):
                frame_color = "red" if (i + j) % 2 == 0 else None
                frame = Frame(self.frame1, bg=frame_color)
                frame.grid(row=i, column=0, sticky="nsew")
                frame.grid_columnconfigure(0, weight=1)

    def show_frame(self):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = self.crop_and_resize(frame, 300, 300)  # Adjust dimensions as needed
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

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
