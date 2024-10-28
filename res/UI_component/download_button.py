from tkinter import Misc
from ..base_class.custom_frame import CustomFrame


class DownloadButton(CustomFrame):
    def __init__(self, master: Misc, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

