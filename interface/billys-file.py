from cgi import test
import tkinter as tk
from tkinter import messagebox
from turtle import delay
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import numpy as np
from test_classifier_adapted import *
import time
import random
from datetime import datetime

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Sign Alphabet")
        self.configure(bg="white")

        self.current_page = None

        self.ret = ""
        self.frame = ""
        self.model = load_model("./model_ElinMatilda500_rf.pickle")
        self.mp_hands = mp.solutions.hands
        self.hand_detection_model = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.on_practice_page = False
        self.on_test_page = False

        self.x1=None
        self.y1=None 
        self.x2=None 
        self.y2=None

        self.correct_sign = False

        #test
        self.test_letters = []
        self.test_timer = 0

        self.camera_page()
        self.start_camera()
        self.show_start_page()  
        
        
        #self.correct_label = tk.Label(self, text="Correct!", font=("Helvetica", 18), fg="green", bg="white")


        self.classifications_list = [] #["","","","","","","",""] 
        self.selected_letter = ""


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
        frame_flipped = cv2.flip(frame, 1)  # flipping frames to display as mirrored
        
        if self.on_practice_page and self.current_page.winfo_class() != 'show_practice_page':
            if (self.x1, self.y1, self.x2, self.y2):                   
                draw_hand_rectangle(frame_flipped, self.x1, self.y1, self.x2, self.y2, self.correct_sign)

        elif self.on_test_page and self.current_page.winfo_class() != 'show_test_page':
            if (self.x1, self.y1, self.x2, self.y2):                   
                draw_hand_rectangle(frame_flipped, self.x1, self.y1, self.x2, self.y2, self.correct_sign)
        
        self.ret = ret
        self.frame = frame_flipped

        if ret:
            image = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = image.resize((640, 480))
            photo = ImageTk.PhotoImage(image)

            self.camera_label.configure(image=photo)
            self.camera_label.image = photo
            self.camera_label.pack()

        self.after(25, self.update_camera)
        

    def increase_font_size(button):
        current_font = button.cget("font")
        new_size = int(current_font.split(" ")[-1]) + 2  # Increase font size by 2
        button.config(font=(new_size))


    def show_start_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.on_test_page = False
        self.number_of_questions = 0
        self.current_question_no = 1
        self.test_letters = []
        self.timer_running = False

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=300)

        credits1 = tk.Label(self.current_page, text="SignAlphabet", background="white", font=("FOT-RodinNTLG Pro DB", 48))
        credits1.grid()

        credits2 = tk.Label(self.current_page, text="A Project by Group 8", background="white", font=("FOT-RodinNTLG Pro DB", 12))
        credits2.grid(pady=20)

        practice_button = tk.Button(self.current_page, text="Practice Signing", bg="lightblue", font=(16), command=self.show_alphabet_page)
        practice_button.grid(pady=5)

        test_button = tk.Button(self.current_page, text="Test Your Abilities", bg="lightyellow", font=(16), command=self.start_test)
        test_button.grid(pady=5)

        quit_button = tk.Button(self.current_page, text="Quit", bg="lightcoral", font=(16), command=self.confirm_quit)
        quit_button.grid(pady=20)


    def show_next_question(self):
        print("Test letters are" + str(self.test_letters))
        if len(self.test_letters) > 0:
            print("Next Question loading.")
            current_test_letter = self.test_letters.pop(0)
            print("Next Question loaded. Showing test page.")
            self.show_test_page(current_test_letter, self.number_of_questions, self.test_timer)
        else:
            print("No more questions. Showing results page.")
            self.after(25, self.show_results_page())


    def start_test(self):
        self.number_of_questions = 3
        self.current_question_no = 0
        self.test_letters = ["A", "L", "A"]
        self.test_timer = 120
        self.original_time = self.test_timer
        self.timer_running = True
        self.show_test_page(self.test_letters[0], len(self.test_letters), self.test_timer)

    def show_test_page(self, current_test_letter, number_of_questions, time):
        if self.current_page:
            self.current_page.destroy()

        self.on_test_page = True
        self.current_question_no += 1
        print("On test page!")

        self.correct_sign = False
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack()

        question_label = tk.Label(self.current_page, text=f"Question {self.current_question_no}"+ "/" + f"{number_of_questions}: What is the sign for: {current_test_letter}", font=("Helvetica", 14), bg="white")
        question_label.grid(row=0, column=0, columnspan=5, pady=(120, 10))

        current_test_letter_label = tk.Label(self.current_page, text=current_test_letter, font=("Helvetica", 36, "bold"), bg="white")
        current_test_letter_label.grid(row=1, column=0, columnspan=5, pady=(0, 100))

        self.time_label = tk.Label(self.current_page, text="Time left:" + str(time) + " seconds", background="white")
        self.time_label.grid()

        next_question_button = tk.Button(self.current_page, text="Next question", bg="lightcoral", font=(16), command=self.show_next_question)
        next_question_button.grid()

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightgreen", font=(16), command=self.reset_and_show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(70, 0))

        self.classify_sign(current_test_letter)
        if self.current_question_no == 1:
            self.update_timer()

    def reset_and_show_start_page(self):
        self.number_of_questions = 0
        self.current_question_no = 1
        self.test_letters = []
        self.timer_running = False
        self.show_start_page()


    def update_timer(self):
        if self.timer_running and self.test_timer > 0:
            self.test_timer -= 1
            self.time_label.config(text=str(self.test_timer))
            self.after(1000, self.update_timer)  # Update the timer every second
        elif self.timer_running and self.test_timer == 0:
            self.show_results_page()


    def show_results_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.correct_sign = False
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=100)


        remaining_time = self.test_timer
        self.score_time =  self.original_time - remaining_time 
        self.timer_running = False


        current_test_letter_label = tk.Label(self.current_page, text="You are on the results page", background="white")
        current_test_letter_label.grid(pady=20)

        remaining_time_label = tk.Label(self.current_page, text=f"Timer paused at {remaining_time} seconds", background="white")
        remaining_time_label.grid(pady=20)

        score_time_label = tk.Label(self.current_page, text=f"You completed the test in {self.score_time} seconds", background="white")
        score_time_label.grid(pady=10)


    def show_alphabet_page(self):
        self.on_practice_page = False
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=100)

        label = tk.Label(self.current_page, text="Pick a letter!", background="white", font=("FOT-RodinNTLG Pro DB", 16))
        label.grid(row=0, column=0, columnspan=5, pady=(120, 50))

        alphabet_buttons = []
        for row in range(6):
            for col in range(5):
                index = row * 5 + col
                if index < 26:
                    letter = chr(65 + row * 5 + col)
                    button = tk.Button(self.current_page, text=letter, bg="lightblue", command=lambda l=letter: self.show_practice_page(l), font=(16))
                    button.grid(row=row + 1, column=col, padx=5, pady=5)

                    alphabet_buttons.append(button)

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightgreen", font=(16), command=self.show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(70, 0))


    def show_practice_page(self, selected_letter):
        self.on_practice_page = True
        self.classifications_list = [None, None, None, None, None, None, None, None] #["", "", "", "", "", "", "", ""]

        if self.current_page:
            self.current_page.destroy()

        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=0, pady=100)

        image_path = f"interface/images/{selected_letter}.png"
        img = Image.open(image_path)
        img = img.resize((200, 200))
        rotated_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        photo = ImageTk.PhotoImage(rotated_img)

        label_text = f"You're learning to sign '{selected_letter}'"
        label = tk.Label(self.current_page, text=label_text, font=("FOT-RodinNTLG Pro DB", 16), bg="white")
        label.grid(row=0, column=0, columnspan=5, pady=(120, 50)) 

        image_label = tk.Label(self.current_page, image=photo, bg="white")
        image_label.photo = photo
        image_label.grid(row=1, column=0, columnspan=5, padx=0, pady=(20, 100)) 

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightgreen", font=(16), command=self.show_alphabet_page)
        go_back_button.grid(row=2, column=0, columnspan=5, pady=(0, 20))
        
        self.classify_sign(selected_letter) 


    def confirm_quit(self):
        result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if result:
            self.destroy()


    def classify_sign(self, letter):
        data_aux = []
        self.x_ = []
        self.y_ = []

        ret = self.ret
        frame = self.frame

        self.H, self.W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hand_detection_model.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS, 
                    self.mp_drawing_styles.get_default_hand_landmarks_style(), 
                    self.mp_drawing_styles.get_default_hand_connections_style())

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)
                    self.x_.append(x)
                    self.y_.append(y)
            self.x1, self.y1, self.x2, self.y2 = find_hand_rectangle(self.x_, self.y_, self.H, self.W)
            classified_letter = classify_letter(self.model, data_aux, self.classifications_list)

            self.correct_sign = self.is_sign_correct(letter, classified_letter)

            if self.correct_sign:
                if self.on_test_page:
                    self.after(25, self.show_next_question)  # Move to the next question after correct sign
        else:
            self.x1, self.y1, self.x2, self.y2 = (None, None, None, None)

        if self.on_practice_page:
            self.after(25, self.classify_sign, letter)  # Continue classifying if on practice page


    def is_sign_correct(self, selected_letter, signed_letter):
        """print("selected:" + str(selected_letter))
        print("classified:" + str(signed_letter))"""

        if selected_letter == signed_letter:
            return True
        else:
            return False
        


if __name__ == "__main__":
    app = Application()
    app.resizable(False, False)
    app.mainloop()