from tkinter import Misc, Label, Entry
from tkinter import filedialog

from ..base_class.custom_frame import CustomFrame


class DownloadPath(CustomFrame):
    def __init__(self, master: Misc, path: str) -> None:
        super().__init__(master)

        self.description = Label(self, text="다운위치: ")
        self.description.pack(side="left")
        self.path = Entry(self, width=70)
        self.path.insert(0, path)
        self.path.pack(side="left")

    def set_path(self, path: str):
        "내용 지우고 내용 입력"
        curr_path = self.path.get()
        self.path.delete(0, len(curr_path))
        self.path.insert(0, path)