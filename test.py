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
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
import glob
import sys


urllib3.disable_warnings()
http = urllib3.PoolManager()


def download_web_images(imgs):
    print('Downloading new images...')
    sys.stdout.flush()
    numImages= 1
    for i in range(len(imgs)):
        if (imgs[i]['src'].find("assets") == -1 and imgs[i]['src'].find("wittyfeed") != -1):
            url_of_image = "https:" + imgs[i]['src'] + "\n" 
            full_name = os.getcwd() + '/images/' + str(numImages) +".jpg"
            urllib.request.urlretrieve(url_of_image,full_name)
            numImages+=1
    return numImages
def generating_transcript(para):
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

    return temp


def remove_all_images():
    print('Deleting old images....')
    files = glob.glob('images/*')
    for f in files:
        os.remove(f)
    print('All images deleted. \n')

url = 'https://www.wittyfeed.com/story/61677/benefits-of-doing-namaz'

def get_data(url):

    #getting response of given url
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "lxml")

    #Implementing BeautifulSoup
    title = soup.title.text
    temp = soup.title.text + "\n"
    para = soup.find_all('p')
    imgs = soup.find_all('img')


    remove_all_images()   #removing all the images before downloading 
    download_web_images(imgs)
    
    #generating_transcript using NLP from text data of article 
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
    
    txt_list =  (temp.split("\n"))
    txt_list = [txt_list[i] for i in range(len(txt_list)) if len(txt_list[i])<=200 and len(txt_list[i])>=30]
    return txt_list

get_data(url)
