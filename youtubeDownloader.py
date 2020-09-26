from pytube import YouTube
import os
from tkinker import *

root=tk()
root.geometry('600x600')

root.title('Youtube Video Downloader')



Lable_1=Lable(root,text = "Please Paste The Youtube Link Here",font=("bold", 20))
Lable_1.place(x=120, y = 20)

myLink = StringVar():
pastelink=Enty(root, width=60, textvariable = myLink)
pastelink.place(x=140, y=80)

def downloadVideo():
    x= str(myLink.get())
    YoutubeVideo = YouTube('https://www.youtube.com/watch?v=waEb2c9NDL8').streams.filter(progressive = True, file_extension='mp4').order_by('resolution').desc().first()
   if not os.path.exists('./downloaded video')
        os.makedirs('./downloaded video')
    YoutubeVideo.download('./downloaded video')

Button(root, text = 'Download Video', width = 20, bg= 'red', fg= 'white', command = downloadVideo).place(x=220, y=110)

root.mainloop