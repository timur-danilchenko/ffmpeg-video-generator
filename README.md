# YouTube Shorts Generator
## Description
Automatic multiple video generation app for youtube shorts. 

Multiple generation means downloading a set of videos and generating videos based on them with a given number of required fragments

There is also the possibility of overlaying an audio track, overlaying text with certain fonts over a video
## Deployment
### Linux
Before launching the application, it is necessary to prepare assets where all materials will be loaded (videos, audios, texts, fonts). 

In order to do this all automatically, and not by hand, you should run the following command

```
make prepare
```

After that, the assets folder is created, which contains the audios, fonts, results, texts, videos folders

```
audios(*.mp3) - contains audio recordings that will be substituted into shorts when generated
fonts(*.ttf) - contains the fonts that will be applied to the text in shorts
results(*.mp4, *.mkv) - results
texts(*.txt) - contains texts that will be supplied in shorts when generated
videos(*.mp4) - contains videos that will be used as the main material when generating shorts videos
```

To run the program, you need to execute the following command
```
make run
```

After that, the application UI will open, which will provide a clear interface for interacting with the application.
### Windows
Soon

## Usage
The application provides a fairly clear interface for easy user interaction with the software