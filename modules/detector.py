import cv2
import mediapipe as mp
import numpy as np
from typing import Tuple, List, Any

class HandDetector:
    def __init__(self, min_detection_confidence: float = 0.7, min_tracking_confidence: float = 0.7, max_num_hands: int = 2):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
            max_num_hands=max_num_hands
        )

    def count_fingers(self, hand_landmarks: Any, hand_label: str) -> int:
        finger_tips = [8, 12, 16, 20]
        finger_dips = [6, 10, 14, 18]
        fingers: List[int] = []

        # Thumb logic
        if hand_label == "Right":
            fingers.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)
        else:
            fingers.append(1 if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x else 0)

        # Other fingers
        for tip, dip in zip(finger_tips, finger_dips):
            fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y else 0)

        return sum(fingers)

    def process_frame(self, frame: np.ndarray) -> Tuple[np.ndarray, int]:
        # Flip and convert
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        total_fingers = 0
        
        if result.multi_hand_landmarks:
            for hand_landmarks, hand_label in zip(result.multi_hand_landmarks, result.multi_handedness):
                label = hand_label.classification[0].label
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                total_fingers += self.count_fingers(hand_landmarks, label)

        return frame, total_fingers
