import random
import time
from typing import List

import ffmpeg
from ..settings import settings

from tqdm import tqdm

from numpy.random import permutation

class VideoGenerator:
    def __init__(self):

        pass

    def run(self, width=1080, height=1920, max_pieces_video_in_one_video: int = 1, min_delay: float = 1, max_delay: float = 10, count: int = 1):
        self.video_sources = list(settings.VIDEOS.glob("*.mp4"))
        self.audios = list(settings.AUDIOS.glob("*.mp3"))

        assert self.video_sources or self.audios, "No one video or audio"
        assert len(self.video_sources) >= max_pieces_video_in_one_video, "The indicator of fragments in one video is more than the videos themselves"

        self.fonts = list(settings.FONTS.glob("*.ttf"))
        self.texts = list(settings.TEXTS.glob("*.txt"))

        assert self.fonts or self.texts, "No one font or text"

        self.width = width
        self.height = height

        self.max_pieces_video_in_one_video = max_pieces_video_in_one_video

        self.min_delay = min_delay
        self.max_delay = max_delay

        for _ in tqdm(range(count)):
            videos = self.convert_videos_to_ffmpeg()
            video = self.concat_videos(videos)
            video = self.draw_text(video)
            self.output_video(video)

    def convert_videos_to_ffmpeg(self) -> List[ffmpeg.Stream]:
        delay = random.uniform(self.min_delay, self.max_delay)

        slice = random.sample(self.video_sources, self.max_pieces_video_in_one_video)
        videos = permutation(slice)

        videos = [ffmpeg.input(video, t=f"{delay:.2f}") for video in videos]
        videos = [ffmpeg.filter(video, "scale", w=self.width, h=self.height) for video in videos]
        return videos

    def concat_videos(self, videos: List[ffmpeg.Stream]) -> ffmpeg.Stream:
        return ffmpeg.concat(*videos)

    def draw_text(self, video):
        font = random.choice(self.fonts)
        text = random.choice(self.texts)

        return ffmpeg.drawtext(video, x=self.width/8, y=self.height/2, fontsize=60, fontcolor="white", textfile=text, fontfile=font)

    def output_video(self, video_stream):
        audio_stream = ffmpeg.input(random.choice(self.audios)).audio

        cover = random.randint(0, (self.min_delay * self.max_pieces_video_in_one_video * 100)) / 100

        try:
            ffmpeg.output(video_stream, audio_stream, str(settings.RESULTS / f"{time.time():.0f}.mp4"), **{"qscale:v": "3", "vsync": "2", "ss": cover, "loglevel": "error"}, shortest=None).run()
        except:
            print("Something went wrong")

    def __iter__(self):
        return self