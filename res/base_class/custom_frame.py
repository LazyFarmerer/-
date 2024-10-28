from tkinter import Frame, Misc
from typing import Any, Literal

class CustomFrame(Frame):
    def __init__(self, master: Misc, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)