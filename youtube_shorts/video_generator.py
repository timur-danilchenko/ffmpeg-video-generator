import random
import time
from pathlib import Path
from typing import List

from glob import glob
import ffmpeg

from .settings import VIDEOS, AUDIOS, RESULTS, TEXTS, FONTS

from itertools import permutations


class VideoGenerator:
    def __init__(self, width=1080, height=1920, max_pieces_video_in_one_video: int = 3, min_delay: float = 1, max_delay: float = 5) -> None:
        # Подгрузка видео идет из папок находиящихся в проекта, в качестве материала
        # Необходимо сохранять видео для монтирования перед запуском
        video_list, audio_list = (list(VIDEOS.glob("**/*.mp4")),
                                  list(AUDIOS.glob("**/*.mp3")))
        fonts_list, texts_list = (list(FONTS.glob("**/*.ttf")),
                                  list(TEXTS.glob("**/*.txt")))


        assert video_list or audio_list, "No one video or audio"
        # assert fonts_list and texts_list, "No one font or text"
        assert len(video_list) >= max_pieces_video_in_one_video, "Max videos in one more than video files"

        # вот здесь идет перестановка видео
        self.videos = permutations(video_list, max_pieces_video_in_one_video)
        self.max_pieces_video_in_one_video = max_pieces_video_in_one_video
        self.audios = audio_list

        self.fonts = fonts_list
        self.texts = texts_list

        self.width = width
        self.height = height

        self.min_delay = min_delay
        self.max_delay = max_delay

    def run(self, width=1080, height=1920, max_pieces_video_in_one_video: int = 5, min_delay: float = 1, max_delay: float = 5, count: int = 1, ended_function=None):
        self.width = width
        self.height = height

        self.min_delay = min_delay
        self.max_delay = max_delay

        # Если во время запуска, меняются настройки обработки видео, то идет обновление
        if max_pieces_video_in_one_video != self.max_pieces_video_in_one_video:
            video_list = list(VIDEOS.glob("**/*.mp4"))
            assert len(video_list) >= max_pieces_video_in_one_video, "Max videos in one more than video files"
            self.videos = permutations(video_list, max_pieces_video_in_one_video)
            self.max_pieces_video_in_one_video = max_pieces_video_in_one_video
        for _ in range(count):
            videos = self.convert_videos_to_ffmpeg()
            video = self.concat_videos(videos)
            video = self.draw_text(video)
            self.output_video(video)
            if ended_function:
                ended_function()

    # Преобразование видео в формат ffmpeg
    def convert_videos_to_ffmpeg(self) -> List[ffmpeg.Stream]:
        # Берем случайное значение из диапазона задержки
        delay = random.uniform(self.min_delay, self.max_delay)
        # logs
        print(delay)

        # ??? надо посмотреть, что за функция
        videos = next(self)
        # создание списка ffmpeg фрагментов, с задержкой(точность до сотен)
        videos = [ffmpeg.input(video, t=f"{delay:.2f}") for video in videos]
        # Обработка видео под формат разрешения
        videos = [ffmpeg.filter(video, "scale", w=self.width, h=self.height) for video in videos]
        return videos

    def concat_videos(self, videos: List[ffmpeg.Stream]) -> ffmpeg.Stream:
        # Почекать работу функции
        return ffmpeg.concat(*videos)

    def draw_text(self, video):
        # Случайный шрифт
        font = random.choice(self.fonts)
        # Случайный текст
        text = random.choice(self.texts)

        # Отрисовка текста
        return ffmpeg.drawtext(video, x=self.width/8, y=self.height/2, fontsize=60, fontcolor="white", textfile=text, fontfile=font)

    def output_video(self, video_stream):
        # Получение аудио потока
        audio_stream = ffmpeg.input(random.choice(self.audios)).audio
        # Наложение на видео

        # Выгрузка видео
        ffmpeg.output(video_stream, audio_stream, str(RESULTS / f"{time.time():.0f}.mp4"), **{"qscale:v": "3", "vsync": "2"}, shortest=None, format='mp4').run()

    def __iter__(self):
        return self

    def __next__(self) -> tuple[Path, ...]:
        # next() функция, разобраться
        return next(self.videos)
