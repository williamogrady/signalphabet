import os  # for using operating system-dependent functionality, such as directories and files
import pickle  # for storing the trained ML-model

import mediapipe as mp
import cv2  # for 
import matplotlib.pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# defining hand detector model
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Saving directory path to our dataset in a variable
DATA_DIR = '../asl_alphabet_train/asl_alphabet_train' 

# Creating variables for the data and the corresponding labels
data = []
labels = []

counter_dict = {} # key: letter, value: number of images where no handlandmarks are detected

# looping through folders of the different letters,
# then through each image in that folder
for dir_ in os.listdir(DATA_DIR)[:3]:
    counter_dict[dir_]=0
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
        data_aux = []
        #x_ = []
        #y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe 
        
        results = hands.process(img_rgb)

        # if landmarks of a hand is found, it loops thorugh each point, 
        # collecting and storing the x- and y- coordinates in an array data_aux
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                """
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)
                    """

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

                    """
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
                    """

            data.append(data_aux)
            labels.append(dir_)
        else:
            counter_dict[dir_]+=1

# Saving the data in a pickle file
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()

"""
print("Number of images where no hand is detected:")
for key, value in counter_dict.items():
    print(key + ":" + str(value))
"""






def test_plot():
    for dir_ in os.listdir(DATA_DIR)[:3]:
        for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:

            img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe 

            
            results = hands.process(img_rgb)

            # Test for drawing images with landmarks 
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    
                    mp_drawing.draw_landmarks(img_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
            else:
                print("no detected hands")
                    
            plt.figure()
            plt.imshow(img_rgb)
            
    plt.show()

#Plot test with specific image (84 points)
img = cv2.imread(os.path.join(DATA_DIR, "C", "C106.jpg"))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe            
results = hands.process(img_rgb)

# Test for drawing images with landmarks 
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(img_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
else:
    print("no detected hands")
        
plt.figure()
plt.imshow(img_rgb)     
plt.show()