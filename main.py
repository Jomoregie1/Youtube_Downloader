import tkinter
from tkinter import ttk
from pytube import YouTube


def onClick():
    global link
    link = url.get()


def close():
    window.quit()


link = ""
window = tkinter.Tk()
window.title("Youtube-Convertor")
frm = ttk.Frame(window)
url = tkinter.Entry(window)
url.insert(0, "Enter Youtube url link here: ")
url.pack()

save = tkinter.Button(window, text="Save", command=onClick)
save.pack()

close_button = tkinter.Button(window, text="Exit", command=close)
close_button.pack()

window.mainloop()

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
