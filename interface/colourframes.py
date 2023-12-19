import tkinter as tk
from tkinter import *

app = tk.Tk()
app.geometry("1200x900")

app.columnconfigure(0, weight = 5)
app.columnconfigure(1, weight = 1)
app.columnconfigure(2, weight = 3)
app.columnconfigure(3, weight = 1)

app.rowconfigure(0, weight = 1)
app.rowconfigure(1, weight = 2)
app.rowconfigure(2, weight = 4)
app.rowconfigure(3, weight = 1)

frame_text_left = tk.Frame(app, bg = "red")
frame_text_middle = tk.Frame(app, bg = "yellow")
frame_text_right = tk.Frame(app, bg = "blue")
frame_text_explenations = tk.Frame(app, bg = "purple")
frame_picture = tk.Frame(app, bg = "lightblue")
frame_text_bottom_right = tk.Frame(app, bg = "black")

frame_text_left.grid(row=0, column=1,sticky = "news")
frame_text_middle.grid(row=0, column=2,sticky = "news")
frame_text_right.grid(row=0, column=3,sticky = "news")
frame_text_explenations.grid(row=1, column=2,sticky = "news")
frame_picture.grid(row=2, column=2,sticky = "news")
frame_text_bottom_right.grid(row=3, column=2,sticky = "news")


app.mainloop()

