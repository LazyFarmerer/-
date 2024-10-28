from tkinter import Misc, LabelFrame, Entry, Button

from ..base_class.custom_frame import CustomFrame
from ..base_class.observer import Subscriber, EventType

class UrlInput(CustomFrame, Subscriber):
    def __init__(self, master: Misc) -> None:
        super().__init__(master)
        Subscriber.__init__(self)

        label_frame = LabelFrame(self, text="영상 주소", padx=10, pady=10)
        label_frame.pack()

        self.url_input = Entry(label_frame, width=70)
        self.url_input.pack(side="left")

        btn = Button(label_frame, text="asd", command=lambda: self.notify(EventType.URL_INPUT))
        btn.pack(side="left")