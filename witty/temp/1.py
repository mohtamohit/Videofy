#!/usr/bin/env python
from moviepy.editor import *
import sys, json, os

text_list = ["Suryaveer", "singh ", "ankit", "mohit mohita"]
clip_list = []

for text in text_list:
    try:
        txt_clip = TextClip(text, fontsize = 72, color = 'white').set_duration(2)
        clip_list.append(txt_clip)
    except UnicodeEncodeError:
        txt_clip = TextClip("Issue with text", fontsize = 72, color = 'white').set_duration(2) 
        clip_list.append(txt_clip)

final_clip = concatenate(clip_list, method = "compose")
final_clip.write_videofile("test.avi", fps = 24, codec = 'mpeg4',audio='123.mp3')


# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("test.avi").subclip(0,15)

# Reduce the audio volume (volume x 0.8)

# Write the result to a file (many options available !)
clip.write_videofile("test.mp4")

try:
    data = json.loads(sys.argv[1])

except:
    print "ERROR"
    sys.exit(1)

# Generate some data to send to PHP
result = {"status":["col 1","col 2"],
  "s":["row 1","row 2"],
  "data":[["a","b"],["c","d"]]}

# Send it to stdout (to PHP)
print json.dumps(result)
