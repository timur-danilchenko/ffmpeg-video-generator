from pathlib import Path

# BASE_DIR = Path(".").resolve()
# ASSETS = BASE_DIR / "assets"
# VIDEOS = ASSETS / "videos"
# AUDIOS = ASSETS / "audios"
# RESULTS = ASSETS / "results"
# FONTS = ASSETS / "fonts"
# TEXTS = ASSETS / "texts"

class Settings:
    def __init__(self):
        self.BASE_DIR = Path(".").resolve()

        self.ASSETS = self.BASE_DIR / "assets"

        self.VIDEOS = self.ASSETS / "videos"
        self.AUDIOS = self.ASSETS / "audios"
        self.FONTS = self.ASSETS / "fonts"
        self.TEXTS = self.ASSETS / "texts"
        self.RESULTS = self.ASSETS / "results"

    def path_videos(self, path):
        self.VIDEOS = Path(path)

    def path_audios(self, path):
        self.AUDIOS = Path(path)

    def path_texts(self, path):
        self.TEXTS = Path(path)

    def path_fonts(self, path):
        self.FONTS = Path(path)

    def path_results(self, path):
        self.RESULTS = Path(path)

settings = Settings()