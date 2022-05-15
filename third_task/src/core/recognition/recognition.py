from collections import Counter
from typing import List, Tuple

from ..utils.load import load
from ..utils.plot import plot
from .HCDClassifier import HCDClassifier
from .ORBClassifier import ORBClassifier
from .SIFTClassifier import SIFTClassifier


def recognition(image: List) -> Tuple[str, List]:
    print("STARTING RECOGNITION")
    """Классификация стиля изображения.

    Args:
        image (List):
            входные изображения.

    Returns:
        Tuple[str, List]:
            метки классов,
            результаты работы дескрипторов.
    """
    # load train sample
    print("LOADING DATABASES")
    data = load()

    # create classifiers for voting classification
    classifiers = {
        "HCD": HCDClassifier(),
        "ORB": ORBClassifier(),
        "SIFT": SIFTClassifier(),
    }

    # split data to X and y
    X_train = [img for img, _ in data]
    y_train = [style for _, style in data]

    # fit classifiers
    for name, classifier in classifiers.items():
        print(f"TRAINING METHOD: {name}")
        classifier.fit(X_train, y_train)
    print("FINISHED TRAINING CLASSIFIERS")

    print("PREDICTING")
    class_marks = {}
    features = []
    for name, classifier in classifiers.items():
        mark_with_feature = classifier.predict(image)
        class_marks[name] = mark_with_feature[0][0]
        features.append(mark_with_feature[0][1])

    # retrieve most common mark
    marks = class_marks

    print(f"MARKS: {class_marks}")

    descriptors = [plot(features[0]), plot(features[1]), plot(features[2])]

    return marks, descriptors
