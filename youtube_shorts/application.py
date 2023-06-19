import sys
from pathlib import Path

import undetected_chromedriver as uc
from .settings import RESULTS, VIDEOS, AUDIOS, FONTS, TEXTS

from PyQt5 import QtWidgets
import threading

from .main_window_design import Ui_MainWindow

BASE_DIR = Path(".").resolve()

class Application(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, video_generator):
        super(Application, self).__init__()
        self.setupUi(self)
        self.update_info()
        self.genVideo.clicked.connect(self.generate_videos)
        self.video_generator = video_generator

    def generate_videos(self):
        width = self.widthVideo.value()
        height = self.heightVideo.value()

        max_pieces_video_in_one_video = self.fragmentInVideo.value()
        min_delay = self.videoDelayMin.value()
        max_delay = self.videoDelayMax.value()
        video_count = self.videoCount.value()

        threading.Thread(target=self.video_generator.run,
                         args=(width, height, max_pieces_video_in_one_video,
                               min_delay, max_delay, video_count, self.update_info)).start()

    
    def update_info(self):
        count_videos = len(list(VIDEOS.glob("**/*.mp4")))
        count_audios = len(list(AUDIOS.glob("**/*.mp3")))
        count_results = len(list(RESULTS.glob("**/*.mp4")))
        count_fonts = len(list(FONTS.glob("**/*.ttf")))
        count_texts = len(list(TEXTS.glob("**/*.txt")))

        self.listWidget.clear()

        accounts_count = self.get_account_count()
        self.listWidget.addItem(f"Количество исходных видео: {count_videos:03d}")
        self.listWidget.addItem(f"Количество аудио дорожек: {count_audios:03d}")
        self.listWidget.addItem(f"Количество шрифтов: {count_fonts:03d}")
        self.listWidget.addItem(f"Количество текстов: {count_texts:03d}")
        self.listWidget.addItem(f"Количество сгенерированных видео: {count_results:03d}")
        self.listWidget.addItem(f"Количество добавленных аккаунтов: {accounts_count:03d}")


def run(video_generator):
    app = QtWidgets.QApplication(sys.argv)
    window = Application(video_generator)
    window.show()
    app.exec_()

if __name__ == '__main__':
    pass
