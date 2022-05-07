import cv2 as cv
import matplotlib.pyplot as plt

face_cascade = cv.CascadeClassifier(
    "first_task/viola_jones/haarcascade_frontalface_default.xml"
)


def run_viola_jones(image):
    image = cv.imread(image)
    image = image.copy()
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (column, row, width, height) in detected_faces:
        cv.rectangle(
            image, (column, row), (column + width, row + height), (255, 0, 0), 3
        )

    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
