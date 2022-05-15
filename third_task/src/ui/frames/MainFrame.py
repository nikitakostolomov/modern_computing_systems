from tkinter import Button, Canvas, Frame, Label, StringVar, W, filedialog
from typing import Callable

import cv2
from PIL import Image, ImageTk

from ...core.recognition.recognition import recognition


class MainFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.state = {
            "image": StringVar(),
        }

        self.tools_frame = Frame(self)
        self.canvas_frame = Frame(self)

        self.mark_label = Label(self.tools_frame, text="Style: ", font="20")

        self.canvas = Canvas(self.canvas_frame, width=1000, height=1000, bg="#CACACA")

        self.tools_frame.grid(column="0", row="0", sticky=W)
        self.canvas_frame.grid(column="1", row="0", sticky=W)

        self.result = []

        self.select_image_button()
        self.run_recognition_button()
        self.mark_label.pack()
        self.canvas.pack()

    def select_image_button(self) -> None:
        self.__button(self.tools_frame, self.select_image, "Select Painting")

    def run_recognition_button(self) -> None:
        self.__button(self.tools_frame, self.run_recognition, "Run Recognition")

    def run_recognition(self) -> None:
        if self.state["image"].get() is None:
            raise Exception("Image not uploaded")

        image = cv2.imread(self.state["image"].get())
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        marks, desc_images = recognition([image])

        res_posx = 300
        res_posy = 150

        print(f"MARKS: {marks}")

        self.mark_label.config(text=f"Style: {marks}")

        # for image in desc_images:
        for index, (method, mark) in enumerate(marks.items()):
            desc = Image.open(desc_images[index])
            desc = desc.resize((270, 270))
            desc = ImageTk.PhotoImage(desc)
            self.result.append(desc)
            self.canvas.create_image(res_posx, res_posy, image=desc)
            res_posy += 150
            self.canvas.create_text(res_posx, res_posy, text=f"{method} – {mark}")
            res_posy += 150

    def select_image(self) -> None:
        self.__filedialog("Select Painting", self.state["image"])

    def __filedialog(self, label: str, var: StringVar) -> None:
        var.set(filedialog.askopenfilename(title=label))

    def __button(
        self, frame: Frame, command: Callable, title="button", width=None, height=None
    ) -> None:
        Button(frame, text=title, width=width, height=height, command=command).pack()
