from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x900")
        self.start_page()
    


    def start_page(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.grid_rowconfigure(0, weight = 1)
        self.frame1.grid_columnconfigure(0, weight = 1) 
        self.frame1.grid_columnconfigure(1, weight = 1)
        
        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.grid(row = 0, column = 0)
        self.practice_btn = ttk.Button(self.frame1, text="Go to Alphabet Page", command=self.alphabet_page)
        self.practice_btn.grid(row = 0, column = 0)

        self.vid = cv2.VideoCapture(0)
        label_widget = Label(self.frame1) # Create a label and display it on app 
        label_widget.grid(row=0, column=0) 
        
        while(True): 
      
    
            ret, frame = self.vid.read() 
  
    
            cv2.imshow('frame', frame) 
      
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

        

        cv2.destroyAllWindows() 


        self.frame1.pack()



        


        


    def alphabet_page(self):
            for i in self.master.winfo_children():
                i.destroy()



    def game_page(self):
            for i in self.master.winfo_children():
                i.destroy()







class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x900")
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.pack()
        self.register_btn = ttk.Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.pack()
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

root = Tk()
App(root)
root.mainloop()