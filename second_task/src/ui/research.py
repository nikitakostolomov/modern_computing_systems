from .app import App
from .frames.ResearchFrame import ResearchFrame


class Research(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_frame = ResearchFrame()
        self.main_frame.pack()
