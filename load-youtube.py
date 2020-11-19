#!/usr/bin/python3
from pytube import YouTube

link = input("entre link youtube:")
youyou = YouTube(link)
videos = youyou.streams.all()

a = 1
for stream in videos:
	print (str(a) +" " +str(stream))
	a += 1
stream_number = int(input("enter number quality video :"))
video = videos[stream_number-1]
video.download("C:/Users/slilo/Videos")

print ("downloaded")


