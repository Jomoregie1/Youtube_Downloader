from pytube import YouTube

link = input("Enter the Url here: ")
youtube = YouTube(link)
views = youtube.views
title = youtube.title
length = youtube.length

print(f"The title of this video {title}")
print(f"The total number of is: {views}")
print(f"The length of this video is: {length}")





