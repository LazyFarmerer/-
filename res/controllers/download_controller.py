import os, json
from typing import Any
from tkinter import Misc, Button, DoubleVar
from tkinter import filedialog

from ..base_class.observer import EventType
from ..base_class.custom_frame import CustomFrame
from ..base_class.observer import Observer
from ..UI_component.download_path import DownloadPath
from ..UI_component.url_input import UrlInput
from ..UI_component.video_description import VideoDescription
from ..UI_component.progress_label import ProgressLabel
from ..utils.download import YouTubeDownload
from ..utils.thumbnail_image import ThumbnailImage

class DownloadController(CustomFrame, Observer):
    def __init__(self, master: Misc, curr_dir: str) -> None:
        super().__init__(master)
        # 각종 변수들
        self.curr_dir = curr_dir
        with open(os.path.join(curr_dir, "res/assets/path.json")) as f:
            path: str = json.loads(f.read())["path"]
        self.curr_progrssbar = DoubleVar()
        self.youTube_download = YouTubeDownload(path)
        self.youTube_download.addObserver(self)
        self.thumbnail = ThumbnailImage()

        # UI 그리기
        self.download_path = DownloadPath(self, path)
        self.download_path.pack(padx=10, pady=10)

        self.urlinput = UrlInput(self)
        self.urlinput.addObserver(self)
        self.urlinput.pack(padx=10, pady=10)

        self.thumbnail = ThumbnailImage().get_path(os.path.join(curr_dir, "res/assets/Youtube_logo.png"))

        self.download_button = Button(self, text="다운받기", command=self.click_download_button)
        self.download_button.pack(side="bottom")
        self.progress_label = ProgressLabel(self, self.curr_progrssbar)
        self.progress_label.pack(side="bottom")

        self.video_description = VideoDescription(self)
        self.video_description.thumbnail.config(image=self.thumbnail.set_image())
        self.video_description.pack(side="left", padx=10, pady=10)

        # 이벤트
        self.urlinput.url_input.bind("<Return>", lambda x: self.update(EventType.URL_INPUT))
        self.download_path.path.bind("<ButtonRelease-1>", self.click_path_entry)


    def update(self, event_type: EventType, data: Any = None):
        match event_type:
            case EventType.URL_INPUT:
                # url 받으면 영상제목 넣고 썸네일 넣고
                url = self.urlinput.url_input.get()
                self.youTube_download.get_url(url)
                self.video_description.video_name.config(text=self.youTube_download.title)
                self.thumbnail.get_url(self.youTube_download.thumbnail_url)
                self.video_description.thumbnail.config(image=self.thumbnail.set_image())

            case EventType.PROGRESS_VIEWER:
                # 다운로드 하는동안 뷰 표시하기
                print(111111)
                value = self.youTube_download.logger.value
                end_value = self.youTube_download.logger.end_value
                percent = value / end_value
                pass_time = self.youTube_download.logger.pass_time
                self.curr_progrssbar.set(percent)
                self.progress_label.progressbar.update()
                self.progress_label.percent.config(text=f"{pass_time:.2f}초 {percent*100:.2f}%")

    def click_download_button(self):
        if not hasattr(self.youTube_download, "yt"):
            return
        self.youTube_download.download()

    def click_path_entry(self, event):
        "마우스 클릭시 실행, 폴더 선택한 후 json 파일에 따로 저장"
        dir_path = filedialog.askdirectory(parent=self,initialdir="/",title='받을 위치 선택')
        if (dir_path == ""):
            return

        self.download_path.set_path(dir_path)
        with open(os.path.join(self.curr_dir, "res/assets/path.json"), "w") as f:
            data = json.dumps({"path": dir_path})
            f.write(data)
