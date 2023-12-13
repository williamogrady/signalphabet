import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)

		# creating a container
		container = tk.Frame(self) 
		self.geometry("1200x900")
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def open_camera(): 
    # Capture the video frame by frame 
    _, frame = vid.read() 
  
    # Convert image from one color space to other 
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
  
    # Capture the latest frame and transform to image 
    captured_image = Image.fromarray(opencv_image) 
  
    # Convert captured image to photoimage 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
  
    # Displaying photoimage in the label 
    label_widget.photo_image = photo_image 
  
    # Configure image in the label 
    label_widget.configure(image=photo_image) 
  
    # Repeat the same process after every 10 seconds 
    label_widget.after(10, open_camera) 

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		self.columnconfigure(0, weight = 5)
		self.columnconfigure(1, weight = 1)
		self.columnconfigure(2, weight = 5)
		self.columnconfigure(3, weight = 1)
		
		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 2)
		self.rowconfigure(2, weight = 4)
		self.rowconfigure(3, weight = 1)
		
		frame_text_left = tk.Frame(self, bg="red")
		frame_text_middle = tk.Frame(self, bg="red")
		frame_text_right = tk.Frame(self, bg="red")
		frame_text_explenations = tk.Frame(self, bg="red")
		frame_picture = tk.Frame(self, bg="red")
		frame_text_bottom_right = tk.Frame(self, bg="red")
	
		frame_text_left.grid(row=0, column=1,sticky = "news")
		frame_text_middle.grid(row=0, column=2, sticky="news")
		frame_text_right.grid(row=0, column=3, sticky="news")
		frame_text_explenations.grid(row=1, column=2, sticky="news")
		frame_picture.grid(row=2, column=2, sticky="news")
		frame_text_bottom_right.grid(row=3, column=2, sticky="news")
		bluebutton = ttk.Button(self, text ="Blue",
							command = lambda : controller.show_frame(Page1))
		bluebutton.grid(row=3, column=2, sticky="news")

# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
