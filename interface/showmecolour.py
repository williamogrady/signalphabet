import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("1200x900")  # Size of the window

my_w.columnconfigure(0,weight=1)
my_w.columnconfigure(1,weight=1)

my_w.rowconfigure(0, weight=1) 
my_w.rowconfigure(1, weight=8) # change weight to 4
my_w.rowconfigure(2, weight=1)

frame_top=tk.Frame(my_w,bg='red')
frame_middle=tk.Frame(my_w,bg='yellow')
frame_bottom=tk.Frame(my_w,bg='blue')
frame_left=tk.Frame(my_w,bg='lightgreen')
#placing in grid
frame_top.grid(row=0,column=1,sticky='WENS')
frame_middle.grid(row=1,column=1,sticky='WENS')
frame_bottom.grid(row=2,column=1,sticky='WENS')
frame_left.grid(row=0,column=0, rowspan=3,sticky='WENS')

my_w.mainloop()  # Keep the window open