from PyQt5.QtCore import QDir, Qt, QUrl, QRect
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon,QPixmap
import sys
from PyQt5 import QtGui,QtCore
import os
from PySide import QtGui, QtCore
MAX_hight = 600
MAX_width = 760

 
class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("Video File") 
        self.setGeometry(0,0,1000,1000)
        self.setFixedHeight(MAX_hight)
        self.setFixedWidth(MAX_width)
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd()+'/123.mp4')))


        self.imgshow(250,500,'lab')
        self.imgsho(250,300,'lab1')


        videoWidget = QVideoWidget()
        videoWidget.setFixedWidth(360)
        videoWidget.setFixedHeight(360)


 
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
 
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
 
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        self.playButton.setEnabled(True)
 
        wid = QWidget(self)
        self.setCentralWidget(wid)
 
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
 
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)
 
        # Set widget to contain window contents
        wid.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        
 

    def exitCall(self):
        sys.exit(app.exec_())
        
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
 
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
 
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
 
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
 
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def imgshow(self,x,y,i):
        # self.setWindowTitle(self.title)

        i=QLabel(self)
        # Create widget
        # label[i] = QLabel(self)
        pixmap = QPixmap('123.png')
        i.setPixmap(pixmap)
        i.setGeometry(x,y,260,150)
        # label.resize(100,100)
        pixmap2 = pixmap.scaledToWidth(64)
        pixmap3 = pixmap.scaledToHeight(64)
        # pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        # label.scaled(64, 64)
 
        self.show()
    def imgsho(self,x,y,i):
        # self.setWindowTitle(self.title)

        i=QLabel(self)
        # Create widget
        # label[i] = QLabel(self)
        pixmap = QPixmap('123.png')
        i.setPixmap(pixmap)
        i.setGeometry(x,y,260,150)
        # label.resize(100,100)
        pixmap2 = pixmap.scaledToWidth(64)
        pixmap3 = pixmap.scaledToHeight(64)
        # pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        # label.scaled(64, 64)
 
        self.show()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())