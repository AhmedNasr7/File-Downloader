from PyQt5.QtCore import *
import urllib.request
import time


class Download_Thread(QThread):

    changedValue = pyqtSignal(float)
    downloadError = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def calculateProgress(self, blocks_count, block_size, total_size):
        if total_size == 0:
            pass
        #size = (blocks_count+1) * block_size
        #self.percent_size = size * 100 / total_size
        self.step = (block_size / total_size)

            self.changedValue.emit(self.step)

    def download(self, url, save_location):

        try:
            urllib.request.urlretrieve(url, save_location, self.calculateProgress)

        except:
            self.downloadError.emit()
            print("Error")

    def run(self):
        pass

