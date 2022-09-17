import tkinter
from tkinter import ttk
from pytube import YouTube

window = tkinter.Tk(screenName="Youtube Downloader")
frm = ttk.Frame(window)
frm.grid()
ttk.Label(frm, text="Enter URL here: ").grid(row=0)
url = tkinter.Entry(window)
url.grid(row=0, column=1)
window.mainloop()

link = url.get()
youtube = YouTube(link)
views = youtube.views
title = youtube.title
length = youtube.length
file = "/Users/joseph/Documents/Youtube_videos"

print(f"The title of this video {title}")
print(f"The total number of is: {views}")
print(f"The length of this video is: {length}")

ys = youtube.streams.get_highest_resolution()
ys.download(file)
print(f"Your Video has been downloaded and can be found{file} ")





