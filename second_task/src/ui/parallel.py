from .app import App
from .frames.ParallelFrame import ParallelFrame


class Parallel(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_frame = ParallelFrame()
        self.main_frame.pack()
