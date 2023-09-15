import mediapipe as mp
import cv2
import numpy as np
from datetime import datetime
import time

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the video mode:
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='../assets/gesture_recognizer.task'),
    running_mode=VisionRunningMode.VIDEO)

# Use OpenCV’s VideoCapture to load the input video.
cap = cv2.VideoCapture('../assets/hand_gesture.mp4')

# Load the frame rate of the video using OpenCV’s CV_CAP_PROP_FPS
# You’ll need it to calculate the timestamp for each frame.
# Write code below:
fps = cap.get(cv2.CAP_PROP_FPS)

# Loop through each frame in the video using VideoCapture#read().
time_stamp_ms = 0

step_cnt = 0
# FRAME_REDUCETION_RATE = 4

start_time = datetime.now()
while cap.isOpened():
    # Read the frame from OpenCV’s VideoCapture.
    success, frame = cap.read()

    # Break out of the loop if there are no more frames.
    if not success:
        break

    # Convert the frame to RGB using OpenCV’s cvtColor().
    # rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to a numpy array using OpenCV’s asarray().
    numpy_frame_from_opencv = np.asarray(frame)

    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_frame_from_opencv)

    with GestureRecognizer.create_from_options(options) as recognizer:
        # Process the image using the gesture recognizer.
        results = recognizer.recognize_for_video(mp_image, time_stamp_ms)

        # Print the gesture label and the timestamp of the frame.
        if results.gestures:
            print(results.gestures[0])
    
    time_stamp_ms += 1000 / fps
    # step_cnt += 1

print(f'Elapsed time: {datetime.now() - start_time}')