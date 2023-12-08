import cv2
import mediapipe as mp
import numpy as np
import pickle


# Read data
model_dict = pickle.load(open("./model_rf_500.p", "rb"))
model = model_dict["model"]

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# defining hand detector model
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Read frames from video input every 25ms
while True:
    data_aux = []
    ret, frame = cap.read()
    frame_flipped = cv2.flip(frame, 1)  # flipping frames to display as mirrored
    frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe     
    results = hands.process(frame_rgb)

    # if landmarks of a hand is found, plot them:
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame_flipped, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS, 
                mp_drawing_styles.get_default_hand_landmarks_style(), 
                mp_drawing_styles.get_default_hand_connections_style())
            
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)
        #TODO Better performance if we only predict samples where all landmarks are detected?
        prediction = model.predict([np.asarray(data_aux)])
        predicted_letter = prediction[0]

    cv2.rectangle(frame_flipped,(x1, y1), (x2, y2), (0,0,0), 4)
    cv2.putText(frame_flipped, predicted_letter, (x1, y1))
    cv2.imshow("frame", frame_flipped)
    cv2.waitKey(1) 

cap.release() 
cv2.destroy()
