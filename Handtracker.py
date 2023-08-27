#Import the Libraries
#Installation:
# 1)OpenCV
# 2)Mediapipe
import cv2
import mediapipe as mp
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands=mp.solutions.hands

cap=cv2.VideoCapture(0)
hands=mphands.Hands()
while True:
    success,image=cap.read()
    #Flip the image horizontally for a later selfie-view display,convert
    #the BGR image to RGB
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    results=hands.process(image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,mphands.HAND_CONNECTIONS)
    cv2.imshow('Handtracker',image)
    cv2.waitKey(1)
