import cv2 as cv
from matplotlib import pyplot as plt

# All the 6 methods for comparison in a list
METHODS = [
    "cv.TM_CCOEFF",
    "cv.TM_CCOEFF_NORMED",
    "cv.TM_CCORR",
    "cv.TM_CCORR_NORMED",
    "cv.TM_SQDIFF",
    "cv.TM_SQDIFF_NORMED",
]
METHODS_TO_TAKE_MIN = [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]


def run_template_matching_methods(img_name, temp_name):
    img = cv.imread(img_name, 0)
    template = cv.imread(temp_name, 0)
    w, h = template.shape[::-1]

    for meth in METHODS:
        img2 = img.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in METHODS_TO_TAKE_MIN:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img2, top_left, bottom_right, 255, 2)
        plt.figure()
        plt.subplot(121), plt.imshow(res, cmap="gray")
        plt.title("Matching Result"), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img2, cmap="gray")
        plt.title("Detected Point"), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()
