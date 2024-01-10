from cgi import test
import select
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

        self.classification_count = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self.classification_count_var = tk.StringVar()

   
        self.available_test_letters = []
        self.test_letters = []
        self.test_timer = 0
        self.high_score_list = self.load_high_scores()
        

      

        self.camera_page()
        self.start_camera()
        self.show_start_page()  
        
        
        


        self.classifications_list = [] 
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
        frame_flipped = cv2.flip(frame, 1) 
        
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
        self.current_page.pack(padx=10, pady=200)

        credits1 = tk.Label(self.current_page, text="SignAlphabet", background="white", font=("FOT-RodinNTLG Pro DB", 48))
        credits1.grid()

        credits2 = tk.Label(self.current_page, text="A Project by Group 8", background="white", font=("FOT-RodinNTLG Pro DB", 12))
        credits2.grid(pady=20)

        practice_button = tk.Button(self.current_page, text="Practice Signing", bg="lightblue", font=("FOT-RodinNTLG Pro DB", 16), command=self.show_alphabet_page)
        practice_button.grid(pady=5)

        test_button = tk.Button(self.current_page, text="Test Your Abilities", bg="lightyellow", font=("FOT-RodinNTLG Pro DB", 16), command=self.check_and_start_test)
        test_button.grid(row=3, pady=10, sticky="n")

        quit_button = tk.Button(self.current_page, text="Quit", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.confirm_quit)
        quit_button.grid(row=4, pady=30)

        credits3 = tk.Label(self.current_page, text="Version 1.1", background="white", font=("FOT-RodinNTLG Pro DB", 12))
        credits3.grid(pady=(50,0))

    def check_and_start_test(self): 
        
        if len(self.available_test_letters) < 3:
            if self.current_page:
                self.current_page.destroy()

                self.current_page = tk.Frame(self, width=600, height=900, background="white")
                self.current_page.pack(padx=10, pady=200)
            
                
                error_label = tk.Label(self.current_page, text="You haven't practiced any letters yet!", font=("FOT-RodinNTLG Pro DB", 14), fg="red", bg="white")
                error_label.grid(row=2, column=0, columnspan=5, pady=(0, 20))

                error_label = tk.Label(self.current_page, text="Learn at least 3 letters first.", font=("FOT-RodinNTLG Pro DB", 12), bg="white")
                error_label.grid(row=3, column=0, columnspan=5, pady=(20, 70))

                expert_button = tk.Button(self.current_page, text="Let's do it anyway!", bg="lightyellow", font=("FOT-RodinNTLG Pro DB", 12), command=self.start_expert_test)
                expert_button.grid(row=4, column=0, columnspan=5, pady=(50, 0))

                note_label = tk.Label(self.current_page, text="This button will start the Expert Test.", font=("FOT-RodinNTLG Pro DB", 12), bg="white")
                note_label.grid(row=5, column=0, columnspan=5, pady=(30, 10))
                
                note2_label = tk.Label(self.current_page, text="5 random questions in 60 seconds.", font=("FOT-RodinNTLG Pro DB", 12), bg="white")
                note2_label.grid(row=6, column=0, columnspan=5, pady=(5, 10))

                go_back_button = tk.Button(self.current_page, text="Back to Start", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.reset_and_show_start_page)
                go_back_button.grid(row=7, column=0, columnspan=5, pady=(50, 0))
        
        else:
           
            self.start_test()


    def show_next_question(self):
        if self.current_page:
            self.current_page.destroy()

        self.timer_running = True

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=100)

        self.time_label = tk.Label(self.current_page, text="Time left:" + str(time) + " seconds", font=("FOT-RodinNTLG Pro DB", 16), background="white")
        self.time_label.grid(columnspan=5, pady=(20, 0)) 

        correct_label = tk.Label(self.current_page, text="Correct! The next letter is ...", font=("FOT-RodinNTLG Pro DB", 24), fg="green", bg="white")
        correct_label.grid(row=0, column=0, columnspan=5, pady=(200, 0))

        print("Test letters are" + str(self.test_letters))
        if len(self.test_letters) > 1:
            print("Next Question loading.")
            self.test_letters.pop(0)
            print("Next Question loaded. Showing test page.")
            self.after(3000, self.show_test_page, self.test_letters[0], self.number_of_questions, self.test_timer)
        else:
            print("No more questions. Showing results page.")
            self.after(25, self.show_results_page)

    def start_test(self):
        self.available_test_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if self.get_button_color(letter) == "lightgreen"]
        self.number_of_questions = min(3, len(self.available_test_letters))
        self.current_question_no = 0
        self.test_letters = random.sample(self.available_test_letters, self.number_of_questions)
        self.test_timer = 120
        self.original_time = self.test_timer
        self.timer_running = True
        self.show_test_page(self.test_letters[0], len(self.test_letters), self.test_timer)

    def start_expert_test(self):
        self.available_test_letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5)
        self.number_of_questions = 5
        self.current_question_no = 0
        self.test_letters = random.sample(self.available_test_letters, self.number_of_questions)
        self.test_timer = 60
        self.original_time = self.test_timer
        self.timer_running = True
        self.show_test_page(self.test_letters[0], len(self.test_letters), self.test_timer)

    def show_test_page(self, current_test_letter, number_of_questions, time):
        if self.current_page:
            self.current_page.destroy()

        self.on_test_page = True
        self.current_question_no += 1

        self.correct_sign = False   
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=150)

        self.time_label = tk.Label(self.current_page, text="Time left:" + str(time) + " seconds", font=("FOT-RodinNTLG Pro DB", 16), background="white")
        self.time_label.grid(columnspan=5, pady=20)        

        question_label = tk.Label(self.current_page, text=f"Question {self.current_question_no}"+ "/" + f"{number_of_questions}: What is the sign for: {current_test_letter}", font=("FOT-RodinNTLG Pro DB", 14), bg="white")
        question_label.grid(row=0, column=0, columnspan=5, pady=(120, 10))

        current_test_letter_label = tk.Label(self.current_page, text=current_test_letter, font=("FOT-RodinNTLG Pro DB", 36, "bold"), bg="white")
        current_test_letter_label.grid(row=1, column=0, columnspan=5, padx=0, pady=(20, 100)) 

        go_back_button = tk.Button(self.current_page, text="Give Up", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.reset_and_show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(50, 0))

        self.next_question_call = False

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
            self.after(1000, self.update_timer)  
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

        remaining_time = self.test_timer
        self.score_time =  self.original_time - remaining_time 
        self.timer_running = False

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=100)

    
        results_label = tk.Label(self.current_page, text="Results", font=("FOT-RodinNTLG Pro DB", 36, "bold"), fg="black", bg="white")
        results_label.grid(row=0, column=0, columnspan=5, pady=(120, 50)) 

       
        completed_time_label = tk.Label(self.current_page, text=f"You completed the test in {self.score_time} seconds.", font=("FOT-RodinNTLG Pro DB", 14), bg="white")
        completed_time_label.grid(row=1, column=0, columnspan=5, pady=(10, 20))

        
        self.scoreboard_frame = tk.Frame(self.current_page, bg="white", width=400, height=400)
        self.scoreboard_frame.grid(row=2, column=0, columnspan=5, pady=(20, 0))

      
        scoreboard_title_label = tk.Label(self.scoreboard_frame, text="Scoreboard", font=("FOT-RodinNTLG Pro DB", 16, "bold"), bg="white")
        scoreboard_title_label.grid(row=0, column=0, pady=(10, 10))


        enter_name_label = tk.Label(self.scoreboard_frame, text="Enter your name", font=("FOT-RodinNTLG Pro DB", 12), bg="white")
        enter_name_label.grid(row=1, column=0, pady=(10, 5))

   
        name_entry = tk.Entry(self.scoreboard_frame, font=("FOT-RodinNTLG Pro DB", 12), width=5)
        name_entry.grid(row=2, column=0, pady=(0, 10))

        go_back_button = tk.Button(self.current_page, text="Back to Start", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(20, 0))

        def submit_name():
            name = name_entry.get()[:5]
            if name == "":
                name = "User"
            self.update_high_score_list(name, self.score_time)
            self.display_high_scores()

       
        self.current_page.bind('<Return>', lambda event=None: submit_name())

   
        submit_button = tk.Button(self.scoreboard_frame, text="Submit", command=submit_name, font=("FOT-RodinNTLG Pro DB", 12), bg="lightgreen")
        submit_button.grid(row=3, column=0, pady=(0, 10))

    def update_high_score_list(self, name, score_time):
  
        self.high_score_list.append((name, score_time, self.number_of_questions))
    
        self.high_score_list.sort(key=lambda x: x[1])
   
        self.high_score_list = self.high_score_list[:5]
  
        self.save_high_scores()

    def load_high_scores(self):
        try:
            with open('high_scores.pickle', 'rb') as file:
                high_scores = pickle.load(file)
            return high_scores
        except (FileNotFoundError, EOFError):
            return []

    def save_high_scores(self):
        with open('high_scores.pickle', 'wb') as file:
            pickle.dump(self.high_score_list, file)

    def display_high_scores(self):
        if self.current_page:
            self.current_page.destroy()

        
        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=100)


        results_label = tk.Label(self.current_page, text="Results", font=("FOT-RodinNTLG Pro DB", 36, "bold"), fg="black", bg="white")
        results_label.grid(row=0, column=0, columnspan=5, pady=(120, 50)) 

      
        scoreboard_title_label = tk.Label(self.current_page, text="Scoreboard", font=("FOT-RodinNTLG Pro DB", 16, "bold"), bg="white")
        scoreboard_title_label.grid(row=1, column=0, columnspan=5, pady=(10, 20))

        for i, (name, score_time) in enumerate(self.high_score_list):
            score_label = tk.Label(self.current_page, text=f"{i + 1}. {name}: {score_time} seconds", font=("FOT-RodinNTLG Pro DB", 12), bg="white")
            score_label.grid(row=i + 1, column=0, pady=(0, 5))

        restart_button = tk.Button(self.current_page, text="Restart Test", bg="lightblue", font=("FOT-RodinNTLG Pro DB", 12), command=self.start_test)
        restart_button.grid(row=6, column=0, columnspan=5, pady=(30, 0))

        go_back_button = tk.Button(self.current_page, text="Back to Start", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.reset_and_show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(20, 0))


    def show_alphabet_page(self):
        self.on_practice_page = False
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self, width=600, height=900, background="white")
        self.current_page.pack(padx=10, pady=100)

        label = tk.Label(self.current_page, text="Pick a letter to learn!", background="white", font=("FOT-RodinNTLG Pro DB", 16))
        label.grid(row=0, column=0, columnspan=5, pady=(120, 50))

        alphabet_buttons = []
        for row in range(6):
            for col in range(5):
                index = row * 5 + col
                if index < 26:
                    letter = chr(65 + row * 5 + col)
                    button_color = self.get_button_color(letter)
                    button = tk.Button(self.current_page, text=letter, bg=button_color, command=lambda l=letter: self.show_practice_page(l), font=("FOT-RodinNTLG Pro DB", 16))
                    button.grid(row=row + 1, column=col, padx=5, pady=5)

                    alphabet_buttons.append(button)

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.reset_and_show_start_page)
        go_back_button.grid(row=7, column=0, columnspan=5, pady=(20, 0))



    def get_button_color(self, letter):
            count = self.classification_count[letter]
            if count >= 20:
                self.available_test_letters.append(letter)
                return "lightgreen"
            else:
                return "lightblue"

    def get_alphabet_button(self, letter):
        
        for widget in self.current_page.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") == letter:
                return widget

      
        new_button = tk.Button(self.current_page, text=letter, bg="lightblue", command=lambda l=letter: self.show_practice_page(l), font=("FOT-RodinNTLG Pro DB", 16))
        return new_button


    def show_practice_page(self, selected_letter):
        self.on_practice_page = True
        self.classifications_list = [None, None, None, None, None, None, None, None] #["", "", "", "", "", "", "", ""]

        if self.current_page:
            self.current_page.destroy()

        self.selected_letter = selected_letter

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
        image_label.grid(row=1, column=0, columnspan=5, padx=0, pady=(20, 60)) 


        self.update_classification_count_on_page(selected_letter)

        go_back_button = tk.Button(self.current_page, text="Go Back", bg="lightcoral", font=("FOT-RodinNTLG Pro DB", 12), command=self.show_alphabet_page)
        go_back_button.grid(row=4, column=0, columnspan=5, pady=(50, 20), sticky="ns")
        
        self.classify_sign(selected_letter) 


    def update_classification_count_on_page(self, letter):
        
        current_count = self.classification_count[letter]

       
        self.classification_count_var.set(current_count)

       
        if self.selected_letter == letter and current_count >= 20:
            self.show_success_message(letter)

       
        self.after(1000, self.update_classification_count_on_page, letter)
        

    def show_success_message(self, letter):
        if self.on_practice_page:
            success_label = tk.Label(self.current_page, text=f"Successfully learned {letter}!", font=("FOT-RodinNTLG Pro DB", 12, "bold"), fg="green", bg="white")
            success_label.grid(row=3, column=0, columnspan=5, pady=(0, 0), sticky="ns")


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

        else:
            
            self.x1, self.y1, self.x2, self.y2 = (None, None, None, None)
         
        if self.correct_sign:
          
            if self.on_practice_page:
                self.classification_count[letter] += 1
                button_color = self.get_button_color(letter)
                button = self.get_alphabet_button(letter)
                button.configure(bg=button_color)
                self.after(25, self.classify_sign, letter)
            elif self.on_test_page:
                print("Classify_sign: Correct, going to next question.")
                
                self.show_next_question()
        
        elif self.on_practice_page or self.on_test_page:
            
            self.after(25, self.classify_sign, letter)
            

    def is_sign_correct(self, selected_letter, signed_letter):


        if selected_letter == signed_letter:
            return True
        else:
            return False
        


if __name__ == "__main__":
    app = Application()
    app.resizable(False, False)
    app.mainloop()