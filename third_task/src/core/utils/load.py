import os
from typing import List, Tuple

import cv2

from ..config import DATABASES


def load() -> List:
    """Выгрузка данных.

    Returns:
        List:
            список, содержащий изображения каждого стиля и метку стиля.
    """
    data = []
    for style in DATABASES:
        for filename in os.listdir(DATABASES[style]):
            f = os.path.join(DATABASES[style], filename)
            img = cv2.imread(f)
            data.append((img, style))
    return data
