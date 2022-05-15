import io

import matplotlib.pyplot as plt
import numpy as np


def plot(image: np.array) -> io.BytesIO:
    fig = plt.figure(figsize=(3, 3))
    plt.imshow(image)
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return buf
