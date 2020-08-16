#!/usr/bin/python3
from pytube import YouTube


#23456789112345678921234567893123456789412345678951234567896123456789712

video=YouTube('https://www.youtube.com/watch?v=FQmupn3YSuY')
itags=video.streams
for x in itags:
    print(x)

