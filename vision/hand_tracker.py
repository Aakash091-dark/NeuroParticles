import cv2
import mediapipe as mp
import numpy as np

class HandTracker:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(0)

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)

    def get_hand_data(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, None

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0]

            index_tip = lm.landmark[8]
            target = np.array([
                index_tip.x * self.width,
                index_tip.y * self.height
            ])

            fingers = 0
            for tip in [8, 12, 16, 20]:
                if lm.landmark[tip].y < lm.landmark[tip - 2].y:
                    fingers += 1

            return target, fingers

        return None, None
