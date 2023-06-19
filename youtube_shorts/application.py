import asyncio
import json
import random
import sys
import time
from pathlib import Path

from .youtube_bot import YouTubeBot
import undetected_chromedriver as uc
from .settings import RESULTS, VIDEOS, AUDIOS, FONTS, TEXTS

from PyQt5 import QtWidgets
import threading

from .main_window_design import Ui_MainWindow

BASE_DIR = Path(".").resolve()
SESSIONS_PATH = BASE_DIR / "sessions"
SESSIONS_PATH.mkdir(exist_ok=True)
ACCOUNTS = Path(__file__).parent.resolve() / "accounts" / "accounts.json"
ACCOUNTS.touch(exist_ok=True)
with open(ACCOUNTS, "r+", encoding="utf-8") as accounts_file:
    if not accounts_file.read():
        json.dump([], accounts_file)


class Application(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, video_generator):
        super(Application, self).__init__()
        self.setupUi(self)
        self.update_info()
        self.addAccount.clicked.connect(self.add_account)
        self.delAccount.clicked.connect(self.del_account)
        self.genVideo.clicked.connect(self.generate_videos)
        self.uploadVideo.clicked.connect(self.upload_video)
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

    def upload_video(self):
        email, password = self.get_random_account().values()
        title = self.videoTitle.text()
        description = self.videoDescription.toPlainText()
        access = (self.privateAccess.isChecked(), self.linkAccess.isChecked(), self.publicAccess.isChecked())
        video_count = self.videoCount.value()
        h, m = self.scheduleUploadVideo.text().split(":")
        schedule_upload_video = int(h), int(m)
        threading.Thread(target=upload_video, args=(email, password, title, description,
                                                    access, video_count, schedule_upload_video,
                                                    self.update_info)).start()

    def get_email(self):
        return self.email.text().strip()

    def get_password(self):
        return self.password.text().strip()

    def get_account_count(self):
        with open(ACCOUNTS, "r", encoding="utf-8") as file:
            accounts = json.load(file)
            return len(accounts)

    def get_random_account(self):
        with open(ACCOUNTS, "r", encoding="utf-8") as file:
            accounts = json.load(file)
            if not accounts:
                raise NotImplemented
            return random.choice(accounts)

    def del_account(self):
        with open(ACCOUNTS, "r+", encoding="utf-8") as file:
            email = self.get_email()
            accounts = json.load(file)
            file.seek(0)
            for account in accounts:
                if account["email"] == email:
                    accounts.remove(account)
                    file.truncate()
                    json.dump(accounts, file, indent=4)
                    break
            else:
                return
        self.update_info()

    def add_account(self):
        with open(ACCOUNTS, "r+", encoding="utf-8") as file:
            email, password = self.get_email(), self.get_password()
            if not (email and password):
                return
            accounts = json.load(file)
            file.seek(0)
            accounts.append({"email": email, "password": password})
            file.truncate()
            json.dump(accounts, file, indent=4)
        self.update_info()

    def update_info(self):
        count_videos = len(list(VIDEOS.glob("**/*.mp4")))
        count_audios = len(list(AUDIOS.glob("**/*.mp3")))
        count_videos_output = len(list(RESULTS.glob("**/*.mp4")))
        count_fonts = len(list(FONTS.glob("**/*.ttf")))
        count_texts = len(list(TEXTS.glob("**/*.txt")))

        self.listWidget.clear()

        accounts_count = self.get_account_count()
        self.listWidget.addItem(f"Количество исходных видео: {count_videos:03d}")
        self.listWidget.addItem(f"Количество аудио дорожек: {count_audios:03d}")
        self.listWidget.addItem(f"Количество шрифтов: {count_fonts:03d}")
        self.listWidget.addItem(f"Количество текстов: {count_texts:03d}")
        self.listWidget.addItem(f"Количество сгенерированных видео: {count_videos_output:03d}")
        self.listWidget.addItem(f"Количество добавленных аккаунтов: {accounts_count:03d}")


def run(video_generator):
    app = QtWidgets.QApplication(sys.argv)
    window = Application(video_generator)
    window.show()
    app.exec_()


def upload_video(email, password, title, description, visibility, video_count, schedule_upload_video, ended_function):
    print(schedule_upload_video)
    print(schedule_upload_video[0] * 60 * 60 + schedule_upload_video[1] * 60)
    options = uc.ChromeOptions()

    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(f'--user-data-dir={SESSIONS_PATH}')

    driver = uc.Chrome(options=options)

    for _ in range(video_count):
        print("Первое видео начало выкладываться")
        try:
            video = list(RESULTS.glob("**/*.mp4"))
            if not video:
                raise NotImplemented
            video = random.choice(video)
            bot = YouTubeBot(driver, email, password)
            bot.upload_video(str(video), title, description, visibility)
            video.unlink(missing_ok=True)
            ended_function()
            print("Видео успешно выложено!")
        except Exception as error:
            print(error)
        time.sleep(schedule_upload_video[0] * 60 * 60 + schedule_upload_video[1] * 60)
    print("Все видео выложены!")
    driver.quit()


if __name__ == '__main__':
    pass
