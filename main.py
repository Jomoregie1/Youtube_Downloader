import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

from pytube import YouTube


# This method is used to take time in seconds and convert it into hours, minutes and seconds.
def Convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


# This on click method is used to assign the youtube url entered in the entry widget to a variable
def OnClick():
    global link
    link = url.get()


# This method destroys the instance of a window created
def Close():
    window.destroy()


# This method allows the user to access files
def Browse():
    global dir_name
    dir_name = filedialog.askdirectory(initialdir="/", title="select a file")
    dir_path.set(dir_name)


# This method contains all the widgets
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

# Sets gets the link variable from youtube using pytube
youtube = YouTube(link)

# Retrives information on the video we are looking to download
views = youtube.views
title = youtube.title
file = dir_name

# Outputs information about the video
print(f"The title of this video is {title}")
print(f"The total number of views is: {views}")
print(f"The length of this video is: {Convert(youtube.length)}")

# Obtains the highest possible resolution for our video and downloads that file into a file that we specify
ys = youtube.streams.get_highest_resolution()
ys.download(file)
print(f"Your Video has been downloaded and can be found{file}")
