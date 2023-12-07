import cv2
import mediapipe as mp

cap = cv2.VideoCapture(2)  #TODO find correct index for webcam

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# defining hand detector model
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Read frames from video input every 25ms
while True:
    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe      
    results = hands.process(frame_rgb)
    
    # if landmarks of a hand is found
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame_rgb, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS, 
                mp_drawing_styles.get_default_hand_landmarks_style(), 
                mp_drawing_styles.get_default_hand_connections_style())

    cv2.imshow("frame", frame)
    cv2.waitKey(25)    
cap.release() 
cv2.destroy()
