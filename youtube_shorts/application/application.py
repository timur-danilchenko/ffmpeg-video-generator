import sys
from pathlib import Path

from ..settings import settings

from PyQt5 import QtWidgets
import threading

from glob import glob
from .design.main_window_ui import Ui_MainWindow

class Application(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, video_generator):
        super(Application, self).__init__()
        self.setupUi(self)
        self.update_info()
        self.videoGenerationButton.clicked.connect(self.generate_videos)
        self.videoPathButton.clicked.connect(self.video_path)
        self.audioPathButton.clicked.connect(self.audio_path)
        self.textPathButton.clicked.connect(self.text_path)
        self.fontsPathButton.clicked.connect(self.fonts_path)
        self.video_generator = video_generator

    def generate_videos(self):
        settings.path_results(QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для полученных результатов'))

        width = self.widthSpinBox.value()
        height = self.heightSpinBox.value()

        max_pieces_video_in_one_video = self.fragmentInSpinBox.value()
        min_delay = self.videoDelayMinSpinBox.value()
        max_delay = self.videoDelayMaxSpinBox.value()
        video_count = self.videoCountSpinBox.value()

        # self.video_generator.run(width, height, max_pieces_video_in_one_video, min_delay, max_delay, video_count)
        threading.Thread(target=self.video_generator.run,
                          args=(width, height, max_pieces_video_in_one_video,
                                min_delay, max_delay, video_count)).start()

    def update_info(self):
        videos = len(list(settings.VIDEOS.glob("*.mp4")))
        audios = len(list(settings.AUDIOS.glob("*.mp3")))
        texts = len(list(settings.TEXTS.glob("*.txt")))
        fonts = len(list(settings.FONTS.glob("*.ttf")))

        self.assetsSettings.clear()

        self.assetsSettings.setText(f"Количество исходных видео: {videos:03d}\n"
                                    f"Количество аудио дорожек: {audios:03d}\n" 
                                    f"Количество текстов: {texts:03d}\n" 
                                    f"Количество шрифтов: {fonts:03d}\n")

        # self.assetsSettings.addItem(f"Количество сгенерированных видео: {count_results:03d}")
        # self.assetsSettings.addItem(f"Количество добавленных аккаунтов: {accounts_count:03d}")

    def video_path(self):
        settings.path_videos(QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с исходными видео(*.mp4)'))
        self.update_info()

    def audio_path(self):
        settings.path_audios(QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с аудиозаписями(*.mp3)'))
        self.update_info()

    def text_path(self):
        settings.path_texts(QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с текстами(*.txt)'))
        self.update_info()

    def fonts_path(self):
        settings.path_fonts(QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с шрифтами(*.ttf)'))
        self.update_info()

def run(video_generator):
    app = QtWidgets.QApplication(sys.argv)
    window = Application(video_generator)
    window.show()
    app.exec_()

if __name__ == '__main__':
    pass
