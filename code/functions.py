from pytube import YouTube

link = input("Paste the video link here:  ")
yt = YouTube(link)

print("Title: ", yt.title)
print("RunTime:  ", yt.length)

