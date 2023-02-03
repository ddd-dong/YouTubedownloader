from pytube import YouTube
from sys import argv
import os
import requests

link=''
yt = YouTube(link)
print("Title: ", yt.title)
print("View: ", yt.views)
yd = yt.streams.get_highest_resolution()
check=yd.download(f'{os.path.dirname(__file__)}/video')
print(check)
