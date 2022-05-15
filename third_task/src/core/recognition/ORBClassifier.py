from typing import List

import cv2
import numpy as np

from .BaseRecognizer import BaseClassifier


class ORBClassifier(BaseClassifier):
    def get_features(self, image: np.ndarray) -> List:
        orb = cv2.ORB_create()
        # find the keypoints with ORB
        kp = orb.detect(image, None)
        # compute the descriptors with ORB
        kp, des = orb.compute(image, kp)

        des = cv2.resize(des, (300, 300))
        des = des.reshape(300, 300)

        return des
