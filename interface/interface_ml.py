import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Sign Alphabet")

        self.current_page = None

        self.camera_page()
        self.start_camera()
        self.show_start_page()

    def camera_page(self):
        self.camera_frame = tk.Frame(self, width=600, height=900)
        self.camera_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.camera_label = tk.Label(self.camera_frame)
        self.camera_label.pack()

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.update_camera()


    def update_camera(self):
        ret, frame = self.cap.read()

        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = image.resize((640, 480))
            photo = ImageTk.PhotoImage(image)

            self.camera_label.configure(image=photo)
            self.camera_label.image = photo

        self.after(10, self.update_camera)




    def show_start_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self, width=600, height=900)
        self.current_page.pack(padx=10, pady=300)

        label = tk.Label(self.current_page, text="SignAlphabet", font=("FOT-RodinNTLG Pro DB", 48))
        label.grid()

        label = tk.Label(self.current_page, text="A Project by Group 8", font=("FOT-RodinNTLG Pro DB", 12))
        label.grid(pady=20)

        select_button = tk.Button(self.current_page, text="Select Letter", bg="lightblue", command=self.show_alphabet_page)
        select_button.grid(pady=20)

        quit_button = tk.Button(self.current_page, text="Quit", bg="lightcoral", command=self.confirm_quit)
        quit_button.grid(pady=20)



    def show_alphabet_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self, width=600, height=900)
        self.current_page.pack(padx=10, pady=300)

        label = tk.Label(self.current_page, text="Pick a letter!", font=("FOT-RodinNTLG Pro DB", 16))
        label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

        alphabet_buttons = []
        for row in range(6):
            for col in range(5):
                index = row * 5 + col
                if index < 26:
                    letter = chr(65 + row * 5 + col)
                    button = tk.Button(self.current_page, text=letter, bg="lightblue", command=lambda l=letter: self.show_practice_page(l))
                    button.grid(row=row + 1, column=col, padx=5, pady=5)
                    alphabet_buttons.append(button)

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightgreen", command=self.show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(10, 0))



    def show_practice_page(self, selected_letter):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self, width=600, height=900)
        self.current_page.pack(padx=10, pady=300)

        image_path = f"interface/images/{selected_letter}.png"
        img = Image.open(image_path)
        img = img.resize((200, 200))  
        photo = ImageTk.PhotoImage(img)

        image_label = tk.Label(self.current_page, image=photo)
        image_label.photo = photo
        image_label.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        label_text = f"You're learning to sign '{selected_letter}'"
        label = tk.Label(self.current_page, text=label_text, font=("FOT-RodinNTLG Pro DB", 16))
        label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightgreen", command=self.show_alphabet_page)
        go_back_button.grid(row=1, column=0, columnspan=5, pady=(200, 0))

    def confirm_quit(self):
        result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if result:
            self.destroy()

if __name__ == "__main__":
    app = Application()
    app.resizable(False, False)
    app.mainloop()
