import tkinter as tk
import cv2
import sklearn

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

frame_flipped = cv2.flip(frame, 1)  # flipping frames to display as mirrored
frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)  # converting to rgb for usage with mediapipe 

if True: 
    cv2.imshow("frame", frame_flipped)
    cv2.waitKey(25) 

cap.release() 

