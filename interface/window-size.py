import customtkinter as tk
import cv2 
from PIL import Image, ImageTk 

# We are designing the frame "Practice Mode 2 " from FIGMA!

vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 10)  # Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 100) 

root = tk.CTk()
root.title("Sign Alphabet")
root.geometry("1200x800")
root.bind('<Escape>', lambda e: root.quit())  # Bind the app with Escape keyboard to quit app whenever pressed 

_, frame = vid.read() # Positional arguments: boolean, matrix of information

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)

button = tk.CTkFrame(root, width = 10, height = 100, bg_color="red")
button.grid(row=0, column=1, sticky="nsew")




"""
gamehalf = tk.CTkFrame(root, bg_color = "red")
gamehalf.grid(row = 0, column = 0, sticky = "nesw")
camerahalf = tk.CTkFrame(root, bg_color = "green")
camerahalf.grid(row = 0, column = 1, sticky = "nesw")
"""


  
    # Convert image from one color space to other 
opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

root.mainloop() 


"""
class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("small example app")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = tk.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        self.combobox = tk.CTkComboBox(master=self, values=["Sample text 1", "Text 2"])
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.button = tk.CTkButton(master=self, command=self.button_callback, text="Insert Text")
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()

    """