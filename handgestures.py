from numba import njit
import cv2
import mediapipe as mp
import pyautogui
import webbrowser
from functools import cache

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

executed = False  # Flag to track execution

while not executed:  # Execute only once

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            finger_count = 0

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id in [8, 12]:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id in [4, 8, 12, 16, 20]:
                    if landmark.y < landmarks[id - 2].y:
                        finger_count += 1

            if finger_count == 5:
                # Open YouTube
                webbrowser.open('https://www.youtube.com')
                executed = True
                break
            if finger_count == 4:
                # Open WhatsApp
                webbrowser.open('https://web.whatsapp.com')
                executed = True
                break
            if finger_count == 1:
                # Open WhatsApp
                webbrowser.open('https://google.com')
                executed = True
                break
            
    cv2.imshow('HandGesture', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
