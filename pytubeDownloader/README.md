# YouTube Downloader

This is a simple YouTube downloader application that allows users to download videos from YouTube by providing a link to the video. The application is built using Python, Tkinter and the PyTube library.

## Requirements

- Python 3.x
- Tkinter (should come pre-installed with python)
- PyTube library (can be installed using pip: `pip install pytube3`)
- CustomTkinter library (can be installed using pip: `pip install customtkinter`)

## Features

- User interface built using Tkinter
- Download videos in the highest available resolution
- Downloads videos to a custom location
- Displays a message upon successful download
- Displays an error message if an invalid YouTube link is provided


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

1. Clone the repository

git clone https://github.com/SleekGeek-254/pyYoutubeDownloaderV1.git


2. Install the required libraries

```
pip install pytube

pip install tkinter

```

### Running the program

1. Navigate to the project directory

```
cd youtube-downloader
```
2. Run the program

## Usage

1. Run the script using `python main.py`
2. Enter the YouTube link of the video you wish to download in the provided text field
3. Press the download button
4. The video will be downloaded to the location specified in the script (in this case it is 'C:/Documents')

## Future To-Do

- Add a feature to select the download location
- Add a checkbox to open the downloaded video with VLC player
- Add a feature to download videos in specific formats
- Add a feature to download playlists
