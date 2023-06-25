import asyncio
from pathlib import Path

# from youtube_shorts.bot.youtube_bot import YouTubeBot
from youtube_shorts.application import application
from youtube_shorts.generator.generator import VideoGenerator

# SIGN_IN_URL = ""
# UPLOAD_VIDEO_URL = "https://studio.youtube.com/channel/upload"

# async\
async def main():
    vg = VideoGenerator()
    application.run(vg)


if __name__ == '__main__':
    # main()
    asyncio.run(main())
