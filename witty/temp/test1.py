import urllib3
import urllib
import json
import nltk
import sumy
import os
import numpy as np
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 
from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient


# RESOLUTION of the Clip

w = 960
h = 506 # 9/16 screen
moviesize = (w,h)

#Function to download images from the webpage

def download_web_image(url, i):
    full_name = os.getcwd() + "/images/" + str(i) +".jpg"
    urllib.request.urlretrieve(url,full_name)

urllib3.disable_warnings()
http = urllib3.PoolManager()

#Input url

# url = 'https://www.wittyfeed.com/story/61677/benefits-of-doing-namaz'
f = open("data.json","r")
data = f.read()
url = ''

data = json.loads(data)
if(data[0]=='first'):
    url = data[1]
    print(url)


response = http.request('GET', url)
soup = BeautifulSoup(response.data, "lxml")

f1 = open("f1.txt","w+")

#Implementing BeautifulSoup
temp = soup.title.text + "\n"
para = soup.find_all('p')
imgs = soup.find_all('img')


numImages= 1

for i in range(len(imgs)):
    if (imgs[i]['src'].find("assets") == -1 and imgs[i]['src'].find("wittyfeed") != -1):
        download_web_image("https:" + imgs[i]['src'] + "\n", numImages)
        numImages+=1

for i in range(len(para)):
    f1 = open("f1.txt", "w+")
    f1.write(para[i].text + "\n")
    f1.close()
    parser = PlaintextParser.from_file("f1.txt", Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, 2)
    for sentence in summary:
    	if(len(str(sentence)) > 30):
            temp += str(sentence) + "\n\n"

f1 = open("f1.txt", "w+")
f1.write(temp)
f1.close()
cnt = 0

txt_list =  (temp.split("\n"))
txt_list = [txt_list[i] for i in range(len(txt_list)) if len(txt_list[i])<=200 and len(txt_list[i])>=30]

sentence = ""
line = ""


f = open("data.json","r")
data = f.read()
jsonObj = json.loads(data)
# print(jsonObj['1'][0])

justifiedList = []

if(jsonObj[0]=='first'):
    justifiedList.append("second")
    for sent in txt_list:
        line = ""
        for txt in sent.split(" "):
            if len(line)+len(txt)+1<=50:
                line = line +  txt + " "
            else:
                sentence = sentence +line + "\n" 
                line = txt + " "
        sentence = sentence + line 
        justifiedList.append(sentence)
        sentence = ""
    with open('data.json', 'w') as outfile:
        json.dump(justifiedList, outfile)
else:
    for i in range(1,len(jsonObj)):
        x = str(i)
        justifiedList.append(jsonObj[i])
print(len(justifiedList)-1)

if(numImages==1):
    print("No Images found in article")
    exit()

avgSentence = int(np.ceil(len(justifiedList)/(numImages-1)))
totalSentence = len(justifiedList)
print(avgSentence)


clip_txt = []
for i in range(1,len(justifiedList)):
    sentence = justifiedList[i]
    cl = TextClip(sentence, color='white',fontsize=25,  font='Roboto').margin(20,opacity = 0).set_pos(('center','bottom'))
    clip_txt.append(cl)


clip_img = []
for i in range(1,numImages):
    clp = ImageClip("images/"+str(i)+".jpg").resize(width = w, height = h)
    clip_img.append(clp)

witty = ImageClip("wittywall.jpeg").resize(width = w, height = h)

cmp_list = []
cmp_list.append(witty)
time = 2
sent_index = 0 

for i in range(0, numImages-1):
    cmp_list.append(clip_img[i].set_start(time))
    # print(str(i))
    time = time + 2
    for k in range(avgSentence):
        if(totalSentence - i*avgSentence >= (numImages-i-1)*(avgSentence-1)):
            if(k==avgSentence-1):
                break
        cmp_list.append(clip_img[i].set_start(time))
        print(sent_index)
        if(sent_index<len(justifiedList)-1):
            cmp_list.append(clip_txt[sent_index].set_start(time))
            time = time+2
            sent_index += 1 

final = CompositeVideoClip(cmp_list,size = moviesize)

final.set_duration(time+2).write_videofile("test.avi", fps=3,codec="mpeg4",audio='123.mp3')

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("test.avi").subclip(0,time+2)
    # Reduce the audio volume (volume x 0.8))
clip.write_videofile("test.mp4")


# # # SCROLL THE TEXT IMAGE BY CROPPING A MOVING AREA

#txt_speed = 20

#fl = lambda gf,t : gf(t)[int(txt_speed*t):int(txt_speed*t+np.ceil(h)):]
# moving_txt= clip_txt.fl(fl, apply_to=['mask'])


# final  = CompositeVideoClip([
#          witty,
#          stars_darkened.set_start(2),
#          moving_txt.set_pos(('center','bottom')).set_start(3)], #warped_txt
#          size = moviesize)

#stars_darkened = stars.fl_image(lambda pic: (0.7*pic).astype('int16'))