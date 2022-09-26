import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

from pytube import YouTube


def Convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def OnClick():
    global link
    link = url.get()


def Close():
    window.destroy()


def Browse():
    global dir_name
    dir_name = filedialog.askdirectory(initialdir="/", title="select a file")
    dir_path.set(dir_name)


def Widgets():
    global url
    url = tkinter.Entry(window, width=27)
    url.insert(0, "Enter Youtube url link here: ")
    url.grid()

    window.destinationText = Entry(window, width=27, textvariable=dir_path)
    window.destinationText.grid(row=1, column=0)

    download = tkinter.Button(window, text="download", command=OnClick)
    download.grid(row=0, column=1)

    open_file = tkinter.Button(window, text="Browse", command=Browse)
    open_file.grid(row=1, column=1)

    close_button = tkinter.Button(window, text="Exit", command=Close)
    close_button.grid()


url = ""
link = ""
dir_name = ""
window = tkinter.Tk()
window.title("Youtube Convertor")
dir_path = StringVar()
frm = ttk.Frame(window)
Widgets()
window.mainloop()

youtube = YouTube(link)
views = youtube.views
title = youtube.title
file = dir_name

print(f"The title of this video is {title}")
print(f"The total number of views is: {views}")
print(f"The length of this video is: {Convert(youtube.length)}")

ys = youtube.streams.get_highest_resolution()
ys.download(file)
print(f"Your Video has been downloaded and can be found{file}")
