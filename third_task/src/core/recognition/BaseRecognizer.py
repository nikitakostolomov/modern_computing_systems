from abc import ABC, abstractmethod
from typing import Callable, List, Tuple

import numpy as np


class BaseClassifier(ABC):
    def __init__(self) -> None:
        self.train_data: List = []

    @abstractmethod
    def get_features(self, image: np.ndarray) -> List:
        pass

    def __dist(self, arr1: np.array, arr2: np.array) -> float:
        return np.linalg.norm(np.array(arr1) - np.array(arr2))

    def __search(self, test: np.array) -> Tuple:
        d_min = float("inf")
        template_min = None
        template_group = None
        for train, group in self.train_data:
            if (d := self.__dist(train, test)) < d_min:
                d_min = d
                template_min = train
                template_group = group
        return template_min, template_group

    def fit(self, X: List, y: List) -> None:
        train_data = []
        for index, image in enumerate(X):
            train_data.append((self.get_features(image), y[index]))
        self.train_data = train_data

    def predict(self, images: List) -> List:
        predicted_groups = []
        for image in images:
            image_features = self.get_features(image)
            _, group_num = self.__search(image_features)
            predicted_groups.append((group_num, image_features))

        return predicted_groups

    def score(self, true_answers: List, predicted_answers: List) -> float:
        if len(true_answers) != len(predicted_answers):
            raise Exception("Received arguments have different length")
        number_true = 0
        for index, ta in enumerate(true_answers):
            if ta == predicted_answers[index]:
                number_true += 1
        return number_true / len(predicted_answers)
