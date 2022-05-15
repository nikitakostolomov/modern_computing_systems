from typing import List

import cv2
import numpy as np

from .BaseRecognizer import BaseClassifier


class HCDClassifier(BaseClassifier):
    def get_features(self, image: np.ndarray) -> List:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

        des = cv2.cornerHarris(gray, 1000, 1, 0.04)
        des = cv2.dilate(des, None)

        des = cv2.resize(des, (300, 300))
        des = des.reshape(300, 300)

        return des
