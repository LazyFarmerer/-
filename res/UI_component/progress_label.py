from tkinter import Misc, Label, DoubleVar
from tkinter.ttk import Progressbar
from ..base_class.custom_frame import CustomFrame


class ProgressLabel(CustomFrame):
    def __init__(self, master: Misc, currProgrssbar: DoubleVar) -> None:
        super().__init__(master)

        self.time = Label(self, text="임시로 넣은 내용")
        self.time.pack()
        self.progressbar = Progressbar(self, maximum=1, variable=currProgrssbar, length=400)
        self.progressbar.pack()
        self.percent = Label(self)
        self.percent.pack()



