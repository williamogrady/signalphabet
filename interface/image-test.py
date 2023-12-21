import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Sign Alphabet")

        self.current_page = None
        self.selected_letter = None

        #self.camera_page()
        #self.start_camera()
        self.show_start_page()

    #def camera_page(self):
        self.camera_frame = tk.Frame(self, width=640, height=480)
        self.camera_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.camera_label = tk.Label(self.camera_frame)
        self.camera_label.pack()

    #def start_camera(self):
        # Your camera initialization code goes here
        pass

    #def update_camera(self):
        # Your camera update code goes here
        pass

    def show_start_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self, width=200, height=480)
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

        self.current_page = tk.Frame(self, width=200, height=480)
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

        self.current_page = tk.Frame(self, width=200, height=480)
        self.current_page.pack(padx=10, pady=300)

        self.selected_letter = selected_letter

        label_text = f"You're learning to sign '{selected_letter}'"
        label = tk.Label(self.current_page, text=label_text, font=("FOT-RodinNTLG Pro DB", 16))
        label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

        text = tk.Label(app, text="Do this")
        text.grid(row=0, column=1)

        image = Image.open("interface/testpicture.png").resize((400, 400))
        bing = ImageTk.PhotoImage(image)

        label = ttk.Label(app, image=bing)
        label.grid(row=1, column=1)

        # Load and display the image
        image_path = f"interface/images/{selected_letter}.png"
        img = Image.open(image_path)
        img = img.resize((200, 200))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)

        image_label = tk.Label(self.current_page, image=photo)
        image_label.photo = photo
        image_label.grid(row=1, column=0, columnspan=5, pady=(10, 0))

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightgreen", command=self.show_alphabet_page)
        go_back_button.grid(row=2, column=0, columnspan=5, pady=(10, 0))

    def confirm_quit(self):
        result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if result:
            self.destroy()

if __name__ == "__main__":
    app = Application()
    app.resizable(False, False)
    app.mainloop()
