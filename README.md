설명추거

``` python
from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip

def downloadYouTube(url: str):
    바탕화면 = "C:/Users/USER/Desktop"
    yt = YouTube(url)
    # 영상, 소리 각각 다운로드
    yt.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first().download(f"{바탕화면}/video")
    yt.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first().download(f"{바탕화면}/audio")

    # 합치기
    videoFileClip = VideoFileClip(f"{바탕화면}/video/{yt.title}.mp4")
    audioFileClip = AudioFileClip(f"{바탕화면}/audio/{yt.title}.mp4")
    videoFileClip.audio = audioFileClip

    if not os.path.exists(f"{바탕화면}/result"):
            os.makedirs(f"{바탕화면}/result")
    videoFileClip.write_videofile(f"{바탕화면}/result/{yt.title}.mp4")
    videoFileClip.close()
    audioFileClip.close()

url = "https://youtube.com/shorts/mF1kmsbplsY?feature=shared"
downloadYouTube(url)
```

이 코드와 완벽하게 기능 똑같음

여기에 tkinter 을 추가한 ....