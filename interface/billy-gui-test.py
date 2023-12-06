import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('FOT-RodinNTLG Pro DB', 24))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('FOT-RodinNTLG Pro DB', 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Message box", font=('FOT-RodinNTLG Pro DB', 18), variable = self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", font=('FOT-RodinNTLG Pro DB', 18), command=self.show_message)
        self.button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        print(event)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

MyGUI()




































"""

root = tk.Tk() # name for window is "root"

root.geometry("800x600")
root.title("Sign Alphabet GUI Test") 

label = tk.Label(root, text="Sign Alphabet", font=('FOT-RodinNTLG Pro DB', 24))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 12)) # tk.Entry is for single line inputs such as passwords.
textbox.pack() 

practicebutton = tk.Button(root, text="Practice", font=('FOT-RodinNTLG Pro DB', 16))
practicebutton.pack(padx=50, pady=50)

testbutton = tk.Button(root, text="Test", font=('FOT-RodinNTLG Pro DB', 16))
testbutton.pack(padx=30, pady=30)

credits = tk.Label(root, text="A project by Group 8", font=('FOT-RodinNTLG Pro DB', 12))
credits.pack(padx=120, pady=120)

root.mainloop() 
 """