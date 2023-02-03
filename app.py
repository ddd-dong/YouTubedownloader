from pytube import YouTube
from sys import argv
import os
from flask import Flask, render_template,request
import requests
from datetime import datetime

app=Flask(__name__)

# downloading={}

def download_video(yt,fname):
    print("Title: ", yt.title)
    print("View: ", yt.views)
    yd = yt.streams.get_highest_resolution()
    check=yd.download(f'{os.path.dirname(__file__)}/static/video',filename=fname)
    # print(f"{downloading.pop(fname)} have loaded {check}")



@app.route('/',methods=['POST','GET'])
def rounded():
    if request.method=='POST' and request.values['send']=="送出":
        print(request.values['video_link'])
        try:
            # print(requests.get(request.values['video_link'], timeout=10,headers={'user-agent': 'Mozilla/5.0'}).status_code)
            if requests.get(request.values['video_link']).status_code<400:
                yt_video=YouTube(request.values['video_link'])
                yt_video.check_availability()
                print(yt_video.title)
                filename= datetime.now().strftime("%Y%m%d_%H%M%S.mp4")
                # downloading[filename]=yt_video.title
                download_video(yt_video,filename)
                return render_template('index.html',video=True,reply=yt_video.title,filename=filename)
            else:
                print(requests.get(request.values['video_link']))
                return render_template('index.html',video=False,reply='網址錯誤或該影片無法訪問')
        except Exception as msg:
            print(msg)
            print("url worng")
            return render_template('index.html',video=False,reply='網址錯誤')
        # if check_availability( )
        
    return render_template('index.html',video=False,reply='')


if __name__=="__main__":
    app.run(debug=True, port=12140)