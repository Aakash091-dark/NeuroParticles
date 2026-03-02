import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os

class HandTracker:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(0)

        # Build path relative to the root or find hand_landmarker.task
        model_path = "hand_landmarker.task"
        if not os.path.exists(model_path):
            model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "hand_landmarker.task")

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1
        )
        self.detector = vision.HandLandmarker.create_from_options(options)

    def get_hand_data(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, None, None

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        results = self.detector.detect(mp_image)

        if results.hand_landmarks:
            lm = results.hand_landmarks[0]

            index_tip = lm[8]
            target = np.array([
                index_tip.x * self.width,
                index_tip.y * self.height
            ])

            fingers = 0
            for tip in [8, 12, 16, 20]:
                if lm[tip].y < lm[tip - 2].y:
                    fingers += 1

            return target, fingers, frame

        return None, None, frame
