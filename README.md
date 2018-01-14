# Videofy
![Alt text](/videofy.png?raw=true)
</br>
A tool that takes an image-based content article and automatically generates a motion-video out of it. 

### Table of Contents
  - [Description](https://github.com/mohtamohit/Videofy/blob/master/README.md#description)
  - [Salient Features](https://github.com/mohtamohit/Videofy/blob/master/README.md#salient-features)
  - [Technologies used](https://github.com/mohtamohit/Videofy/blob/master/README.md#tech)
  - [How to use Videofy?](https://github.com/mohtamohit/Videofy/blob/master/README.md#how-to-use-videofy)
  - [How it works?](https://github.com/mohtamohit/Videofy/blob/master/README.md#how-it-works)
  - [Contributors](https://github.com/mohtamohit/Videofy/blob/master/README.md#contributors)
  - [Future Work](https://github.com/mohtamohit/Videofy/blob/master/README.md#future-work)

### Description
The online world is brimmed with an enormous number of content and for a non-traditional reader, watching videos is always an easy escape when he or she is in the midst of tons of text up and down. In fact, more and more marketers are seeking easier ways of publishing there content as a video file rather than the long boring texts.

Thus, we would be correct to a very high extent, if we claim, that video content would drag more eye-balls and more attention when compared to the black and white words on paper.

But, making a video is a far more tedious job than writing a blog and so most of the people stick to writing blog or designing infographics, rather than investing their time in presenting the same content in the form of a video.
###### And so, here is where, Videofy would be their rescue.

### Salient Features
- Takes a URL and scrapes all data on that page
- LexRank() to measure the importance of sentences in the graph by considering its relative importance to its neighboring sentences.
- Prepares the complete video for the article with proper summary
- A very handy web app already to serve you
- A chrome/chromium plugin(extension) "Videofy_Chrome_extension.zip"for https://www.wittyfeed.com/story to instantly open the video editing tool Videofy
- Implemented sentimental analysis based on nltk library, python. It determines the mood of the person writing the article. Moreover, the motion video supports the audio files that depict the mood of the person 


### How-to-use-Videofy?
It is as simple as searching on google and more easier than reading an article on Wittyfeed. Well, so if you ever feel a bit tired but you still want to read the viral witty feeds on Wittyfeed.com. You have Videofy to help you out. You just  need to follow these simple steps : 
  - Copy the URL of the article you want to make a video of to the the Videofy website ( we aren't live yet, url for our website will be updated here soon). Till then, until the time we are here in the wittyfeed office (before the end of this hackathon), you can view it at http://192.168.2.12/witty/
  - Simply press enter after pasting the URL there.
  - The video will be rendered in the frame on that page in some time.
  - DIRECTIONS TO USE CHROME-EXTENSION
    To install from sources:
    Go to chrome://extensions/.
    Click Load unpacked extension.
    Select the extension directory.
    Once above steps are performed, just go to https://www.wittyfeed.com/story and press the right most button on the screen.

Really simple, isn't it? :)

### Tech
Videofy uses a number of open source projects to work properly:
* [moviepy-python] - For making movies out of text, images and sound
* [nltk-python] - For sentiment analysis
* [numpy-python] - For math function
* [socket] - For client-server communication
* [urllib-python] - For requesting URLs
* [beautifulsoup-python] - For scraping the web
* [sumy-python] - For text summarisation
* [php, materialize.css, html5] - For designing web page

### How-it-works?
You might be curious to know how this tool works. There do not exist many tools with such a use case and offering such an ease to the users.

We use various specialized techniques in order to achieve our objective. And, here are the details of the same :
  - The first task is to scrape the data on the website. All the text and all the images - the relevant ones (discarding advertisements and any other noise). So, we use BeautifulSoup and urllib to scrape all the data on the given link. Then, we parse it to get the text of the article. And, we also fetch the images used in the article on our servers.
  - Once we have all the data, the next step is to shorten it to the extremely useful stuff so that we can have the captions for the video we make. We use [lexrank()](http://blog.nus.edu.sg/soctalent/2010/02/11/a-brief-summary-of-lexrank-graph-based-lexical-centrality-as-salience-in-text-summarization/) algorithm to analyse the text and sum every image description in two lines. We store these captions, mapping them with the address of the relevant image in a JSON file.
  - A video without an appropriate music in the background is like a musician without his instrument. This becomes a [sentiment-analysis](http://text-processing.com/demo/sentiment/) problem. We used nltk package of python for this and got the mood of the article. With the mood of the article, we can make a relevant music-choice from our database.
  - After music and caption, we had to sync everything to render the final video. So, we used [moviepy](https://github.com/Zulko/moviepy) library of python to bring all the elements of the video together alongwith beautiful animations and other visual effects.
  - Tadaaa, the video will be ready for consumption.

### Contributors
  - [Ankit Gaur](https://github.com/ankit-gaur)
  - [Mohit Mohta](https://github.com/mohtamohit)
  - [Suryaveer Singh](https://github.com/surya-veer)
  - [Priyanshu Varshney](https://github.com/priyanshuvarsh)

### Future-Work
- We already have the website live on our local server.
- Browser extenstions can be made for this tool very easily. This way, the users who have it installed and are browsing some articles, can simply click on the Videofy button (which will be inserted on the webpage using Javascript at client side) and can simply see a video for the very same article.
- An android and iOS client for the same.

