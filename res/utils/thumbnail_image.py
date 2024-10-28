from typing import Self
import requests
from io import BytesIO

from PIL import Image, ImageTk

class ThumbnailImage:
    def __init__(self) -> None:
        self.image: Image.Image
        self.show: ImageTk.PhotoImage

    def get_url(self, url: str) -> Self:
        img = requests.get(url).content
        self.image = Image.open(BytesIO(img))
        self.resize()
        return self

    def get_path(self, path: str) -> Self:
        self.image = Image.open(path)
        self.resize()
        return self

    def resize(self) -> Self:
        width, height = self.image.size
        ratio = height / width

        new_width = 400
        new_height = round(ratio * new_width)
        self.image = self.image.resize((new_width, new_height))

        return self

    def set_image(self) -> ImageTk.PhotoImage:
        self.__check_error()

        self.show = ImageTk.PhotoImage(self.image)
        return self.show

    def __check_error(self):
        if not hasattr(self, "image"):
            raise ValueError("이미지가 없는데여 get_url() 또는 get_path() 사용 후 다시 시도")


if __name__ == "__main__":
    import tkinter
    tkinter.Tk()

    # a = ThumbnailImage().get_path("c:/Code/Python Project/유튭 영상 다운로드/res/assets/Youtube_logo.png")
    a = ThumbnailImage().get_url("https://i.ytimg.com/vi/Lrqj9T7LBps/sddefault.jpg")

    # a = ThumbnailImage()
    # a.image.show()