# Hand Gesture Control System

This project demonstrates a hand gesture-based control system for opening webpages. It utilizes computer vision techniques and hand landmark detection to recognize specific gestures and trigger corresponding actions.

## Dependencies

- numba
- opencv-python (cv2)
- mediapipe
- pyautogui
- webbrowser
- functools

You can install the required dependencies using pip:
pip install numba opencv-python mediapipe pyautogui


## Usage

1. Make sure you have a webcam connected to your system.

2. Clone this repository and navigate to the project directory.

3. Run the `hand_gesture_control.py` script using Python:


4. The program will open the webcam feed and start detecting hand gestures.

5. Perform the following gestures to trigger actions:

   - Open hand with all five fingers extended: Opens YouTube.
   - Four fingers extended: Opens WhatsApp.
   - Single finger extended: Opens Google.

6. The program will open the corresponding webpages in your default browser.

7. Press 'q' to quit the program.

## Notes

- Ensure that your hand is well-lit and positioned within the camera frame for accurate gesture detection.

- The program uses mediapipe's hand detection model to detect hand landmarks. Make sure you have a reliable hand tracking environment for optimal performance.

- The screen resolution is used to map the finger position to the screen coordinates, allowing the program to open webpages based on the detected gestures.

- You can modify the code to add more gestures or customize the actions triggered by each gesture.


