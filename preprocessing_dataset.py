import os  # for using operating system-dependent functionality, such as directories and files
import pickle  # for storing the trained ML-model
import random
import mediapipe as mp
import cv2 

# defining hand detector model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Saving directory path to our dataset in a variable
DATA_DIR = '../asl_alphabet_train/asl_alphabet_train' 

# Creating variables for the data and the corresponding labels
data = []
labels = []

counter_dict = {} # key: letter, value: number of images where no handlandmarks are detected
num_img = 500  # Desired number of images per letter/label 

# looping through folders of the different letters,
# then through each image in that folder
for dir_ in os.listdir(DATA_DIR):
    print(dir_)
    counter_dict[dir_] = 0
    detected_num = 0
    letter_list = os.listdir(os.path.join(DATA_DIR, dir_))
    random.shuffle(letter_list)                        
    #Shuffle list of images before split
    for img_path in letter_list:
        if detected_num >= num_img:  # collect data from the XXX first pictures where 42 handlandmarks are detected 
            break
        else:
            data_aux = []  # list for coordinates of detected hand landmarks 

            img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe 
            
            results = hands.process(img_rgb)

            # if landmarks of a hand is found, it loops thorugh each point, 
            # collecting and storing the x- and y- coordinates in an array data_aux
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x)
                        data_aux.append(y)
                if len(data_aux) == 42:
                    detected_num += 1
                    data.append(data_aux)  # adding a list with coordinates of all landmarks
                    labels.append(dir_)
                else:
                    """print(len(data_aux))
                    print(img_path)"""
                    counter_dict[dir_]+=1
            else:
                counter_dict[dir_]+=1

# Saving the data in a pickle file
f = open('data_rf_500_shuffled.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)  # data: list of lists with coordinates of all landmarks per picture
f.close()


print("Number of images where hand is incorrecly detected or not detected at all:")
for key, value in counter_dict.items():
    print(key + ":" + str(value))


# Datasets:
# data.pickle --> 500 images/letter
# data_rf_500_shuffled.pickle --> 500 images/letters shuffled