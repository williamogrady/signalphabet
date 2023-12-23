import cv2
import mediapipe as mp
import numpy as np
import pickle

def load_model(filepath): # call with variable "./model_rf_500_shuffled.p"
    model_dict = pickle.load(open(filepath, "rb"))
    model = model_dict["model"]
    return model


def handle_landmarks(rgb_frame, mp_drawing, frame, data_aux, x_, y_):
    # Draw landmarks:
    for hand_landmarks in rgb_frame.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, 
            hand_landmarks, 
            mp_hands.HAND_CONNECTIONS, 
            mp_drawing_styles.get_default_hand_landmarks_style(), 
            mp_drawing_styles.get_default_hand_connections_style())
    # Store landmark coordinates:   
    for hand_landmarks in rgb_frame.multi_hand_landmarks:
        for i in range(len(hand_landmarks.landmark)):
            x = hand_landmarks.landmark[i].x
            y = hand_landmarks.landmark[i].y
            data_aux.append(x)
            data_aux.append(y)
            x_.append(x)
            y_.append(y)

def find_hand_rectangle(x_, y_):
    # Finding corners for rectangle around hand
    x1 = int(min(x_)*W)
    y1 = int(min(y_)*H)
    x2 = int(max(x_)*W)
    y2 = int(max(y_)*H)

    #cv2.rectangle(frame_flipped,(x1, y1), (x2, y2), (0,0,0), 4)
    return x1, y1, x2, y2
        

def predict_letter(model, data):
    try:
        prediction = model.predict([np.asarray(data)])
        predicted_letter = prediction[0]
        return predicted_letter
    except ValueError:
        return

        
if __name__ == "__main__":

    model = load_model("./model_rf_500_shuffled.p")

    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    # Defining hand detection model
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    # Read frames from video input every 25ms
    while True:
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        H, W, _ = frame.shape

        frame_flipped = cv2.flip(frame, 1)  # flipping frames to display as mirrored
        frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe     
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:  # if landmarks of a hand is found, plot and store them
            handle_landmarks(frame_flipped, mp_drawing, results, data_aux, x_, y_)
            x1, y1, x2, y2 = find_hand_rectangle(x_, y_)
            predicted_letter = predict_letter(model, data_aux)

            # Show frame with landmarks and predicted letter
            cv2.rectangle(frame_flipped,(x1, y1), (x2, y2), (0,0,0), 4)
            cv2.putText(frame_flipped, predicted_letter, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,0,0), 3, cv2.LINE_AA)
        
        cv2.imshow("frame", frame_flipped)
        cv2.waitKey(25) 

    cap.release() 
    cv2.destroy()





