import customtkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

app = tk.CTk() # Create a GUI app 
app.geometry("800x600")

image = Image.open("interface/testpicture.png").resize((400, 400))
bing = ImageTk.PhotoImage(image)

label = ttk.Label(app, image=bing)
label.pack()

app.mainloop()