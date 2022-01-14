from youtube import videoDownload
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, savePath, url):
        super(Worker, self).__init__()
        self.path = savePath
        self.url = url
        
    def run(self):
        title = videoDownload(self.path, self.url)
        self.finished.emit(title)
