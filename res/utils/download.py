from typing import Any
import os
from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip

from .custom_progress_logger import CustomProgressLogger
from ..base_class.observer import Observer, Subscriber, EventType

class YouTubeDownload(Observer, Subscriber):
    def __init__(self, path: str) -> None:
        Subscriber.__init__(self)
        self.path = path
        self.yt: YouTube
        self.logger = CustomProgressLogger()
        self.logger.addObserver(self)

    def get_url(self, url):
        self.yt = YouTube(url, on_progress_callback=self.logger.on_progress)
        return self

    def download(self):
        "다운로드 시작"
        video_path = f"{self.path}/video"
        audio_path = f"{self.path}/audio"
        print("\n영상만 다운")
        self.yt.streams.filter(only_video=True, file_extension="mp4").order_by('resolution').desc().first().download(video_path) # type: ignore
        print("\n음성만 다운")
        self.yt.streams.filter(only_audio=True, file_extension="mp4").order_by('abr').desc().first().download(audio_path, mp3=True) # type: ignore

        # moviepy로 비디오와 오디오를 로드
        videoFileClip = VideoFileClip(f"{video_path}/{self.yt.title}.mp4")
        audioFileClip = AudioFileClip(f"{audio_path}/{self.yt.title}.mp3")
        videoFileClip.audio = audioFileClip

        # 프로세스 로그 초기화 후 다운로드 + 다 끝난 후 삭제
        print("\n영상 합성 시작")
        if not os.path.exists(f"{self.path}/result"):
            os.makedirs(f"{self.path}/result")

        self.logger.reset_data()
        videoFileClip.write_videofile(f"{self.path}/result/{self.yt.title}.mp4", logger=self.logger)
        audioFileClip.close()
        audioFileClip.close()
        print("\n영상 합성 완료")

    @property
    def title(self) -> str:
        self.__ckeck_error()
        return self.yt.title
    @property
    def thumbnail_url(self) -> str:
        self.__ckeck_error()
        return self.yt.thumbnail_url

    def update(self, event_type: EventType):
        print("보내짐")
        match event_type:
            case EventType.PROGRESS_VIEWER:
                # CustomProgressLogger 한테 받은 이벤트를 다시 부모(DownloadController)에게 보내기
                self.notify(EventType.PROGRESS_VIEWER)

    def __ckeck_error(self):
        if not hasattr(self, "yt"):
            raise ValueError("없음, get_url() 쓰세용")
