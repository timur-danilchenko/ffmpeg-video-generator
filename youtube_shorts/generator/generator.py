import random
import time
from typing import List

import os
import ffmpeg
from ..settings import settings

from tqdm import tqdm

from numpy.random import permutation
from moviepy.editor import VideoFileClip

class VideoGenerator:
    def __init__(self):
        pass

    def run(self, width=1080, height=1920, max_pieces_video_in_one_video: int = 1, count: int = 1):
        self.video_sources = list(settings.VIDEOS.glob("**/*.mp4"))
        self.audios = list(settings.AUDIOS.glob("**/*.mp3"))

        assert self.video_sources or self.audios, "No one video or audio"
        assert len(self.video_sources) >= max_pieces_video_in_one_video, "The indicator of fragments in one video is more than the videos themselves"

        self.fonts = list(settings.FONTS.glob("**/*.ttf"))
        self.texts = list(settings.TEXTS.glob("**/*.txt"))

        assert self.fonts or self.texts, "No one font or text"

        self.width = width
        self.height = height

        self.max_pieces_video_in_one_video = max_pieces_video_in_one_video

        # self.min_delay = min_delay
        # self.max_delay = max_delay

        for _ in tqdm(range(count)):
            videos = self.convert_videos_to_ffmpeg()
            video = self.concat_videos(videos)
            video = self.draw_text(video)
            self.output_video(video)

    def convert_videos_to_ffmpeg(self) -> List[ffmpeg.Stream]:
        # Случайный набор видое со всех исходных видео
        slice = random.sample(self.video_sources, self.max_pieces_video_in_one_video)

        # Случайная перестановка
        videos = permutation(slice)

        # TODO: вот здесь происходит преобразование видео во входной поток
        #  именно здесь можно настроить параметр длительности фрагмента,
        #  но учти что фрагменты все могут быть разной длины

        videos = [ffmpeg.input(video) for video in videos]

        # Наложение фильтра

        videos = [ffmpeg.filter(video, "scale", w=self.width, h=self.height) for video in videos]
        return videos

    def concat_videos(self, videos: List[ffmpeg.Stream]) -> ffmpeg.Stream:
        # Просто объединение видео в одно
        return ffmpeg.concat(*videos)

    def draw_text(self, video):
        # Случайный выбор шрифта
        font = random.choice(self.fonts)

        # Случайный выбор текста
        text = random.choice(self.texts)

        # TODO: если надо можно подвинуть текст
        return ffmpeg.drawtext(video, x=self.width/8, y=self.height/2, fontsize=60, fontcolor="white", textfile=text, fontfile=font)

    def output_video(self, video_stream):
        audio_stream = ffmpeg.input(random.choice(self.audios)).audio

        # TODO: по-хорошему было бы круто получить общую длительность видео
        #  и взять оттуда случайный фрагмент, но в этом ебанном классе video_stream,
        #  хуй ты получишь параметр duration, попробуй посмотреть ffmpeg.probe(),
        #  оттуда как-то можно вытянуть, но я не разобрался
        cover = random.randint(0, 10)

        try:
            # TODO: разобарться как выставить cover с помощью output функции(ss параметр, но этот параметр выставляет start метру для видео)
            ffmpeg.output(video_stream, audio_stream, str(settings.RESULTS / f"{time.time():.0f}.mp4"), **{"qscale:v": "3", "vsync": "2", "ss": f'00:00:{cover:02d}', "loglevel": "error"}, shortest=None).run()
        except:
            print("Video duration must be")

    def delete_trash(self, duration: int = 10):
        for file_path in settings.RESULTS.iterdir():
            if file_path.suffix.lower() == '.mp4':
                video = VideoFileClip(str(file_path))
                video_duration = video.duration
                video.close()

                if video_duration <= duration:
                    os.remove(file_path)

    def __iter__(self):
        return self