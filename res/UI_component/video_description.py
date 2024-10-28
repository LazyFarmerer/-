from tkinter import Misc, LabelFrame, Label, PhotoImage

from ..base_class.custom_frame import CustomFrame
from ..base_class.observer import Subscriber


class VideoDescription(CustomFrame, Subscriber):
    def __init__(self, master: Misc, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        Subscriber.__init__(self)

        label_frame = LabelFrame(self, text="영상 정보", padx=10, pady=10)
        label_frame.pack()

        self.thumbnail = Label(label_frame, image=PhotoImage(file="C:/Code/Python Project/card_crop_1.png"))
        self.thumbnail.pack(side="bottom", anchor="s")
        video_title = Label(label_frame, text="제목: ")
        video_title.pack(side="left")

        self.video_name = Label(label_frame, text="없음")
        self.video_name.pack(side="left")

