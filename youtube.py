import ssl
import pytube
from pytube.cli import on_progress

def videoDownload(savePath, urlList):
    ssl._create_default_https_context = ssl._create_stdlib_context
    yt = pytube.YouTube(urlList[0], on_progress_callback=on_progress)
    yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(savePath)

    return yt.title