import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

# Att göra : en class för KAMERAN, som vi kan importera som frames, 
# och göra så att vi kan ha två pages i appen samtidigt.
# En av dessa ska då vara KAMERAN. 

class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs): 
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self) 
		self.geometry("1200x900")
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
	
		self.frames = {} 
		
        # Inkorporera så att den alltid öppnar (Camera, PAGE)
		for F in (StartPage, AlphabetPage, GamePage):
			frame = F(container, self)
			self.frames[F] = frame 
			frame.grid(row = 0, column = 0, sticky ="nsew")
               
		self.show_frame(StartPage)
          
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Start", font = ("Arial", 14))
        label.pack()
        
        bluebutton = ttk.Button(self, text ="Alphabet", command = lambda : controller.show_frame(AlphabetPage))
        bluebutton.pack()


class AlphabetPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Alphabet", font = ("Arial", 14))
        label.pack()
        
        redbutton = ttk.Button(self, text ="Game", command = lambda : controller.show_frame(GamePage))
        redbutton.pack()


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Game", font = ("Arial", 14))
        label.pack()
       
        greenbutton = ttk.Button(self, text ="Green", command = lambda : controller.show_frame(StartPage))
        greenbutton.pack()

# NY CLASS #
class Camera(tk.Frame):
    def __init__(self, parent, controller):
        vid = cv2.VideoCapture(0).__init__(self, parent)
        label_widget = tk.CTkLabel(app) # Create a label and display it on app 
        label_widget.grid(row=0, column=0) 

        def open_camera(): 
            _, frame = vid.read() 
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
            captured_image = Image.fromarray(opencv_image) 
            photo_image = ImageTk.PhotoImage(image=captured_image) 
            label_widget.photo_image = photo_image 
            label_widget.configure(image=photo_image) 
            label_widget.after(10, open_camera) 




app = tkinterApp()
app.mainloop()