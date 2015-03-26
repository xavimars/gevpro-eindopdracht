import sys
import string
import subprocess
from PyQt4 import QtGui, QtCore
import re
from random import randrange

''' Authors: Luuk Looijenga and Xavier Marseille
    A program for finding two (semi-) rhyming tweets and
    putting them together. '''

class Scherm(QtGui.QWidget):

    def __init__(self):
        super(Scherm, self).__init__()
        self.getTweets()
        
        
    def initUI(self, oList, rList):
        self.setGeometry(100, 100, 1000, 200)
        self.setWindowTitle('TwieTwiet')

        ladyList = []
        
        x = randrange(len(rList))
        y = randrange(len(oList))
       
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(4)
        self.Button_one = QtGui.QPushButton('Quit', self)

        tweet1 = QtGui.QLabel(oList[y], self)
        tweet1.resize(1000, 50)
        tweet1.move(20, 0)

        tweet2 = QtGui.QLabel(rList[x], self)
        tweet2.resize(1000,100)
        tweet2.move(20, 30) 
        
        self.Button_one.move(400, 100)
        self.Button_one.resize(200, 50)

        self.Button_one.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        self.show()      
        
    def getTweets(self):
        tweets = []
        with open('gestolentweets.txt') as infile:
            for line in infile:
                removeUrl = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', line)
                tweets.append(removeUrl)
        self.getLastWord(tweets)

    def getLastWord(self, tweetlist):
        lastWords = [item.split()[-1] for item in tweetlist]
        lastWords = [''.join(c for c in s if c not in string.punctuation) for s in lastWords]
        lastWords = [x for x in lastWords if x]

        self.repeat(lastWords, tweetlist)

    def repeat(self, lastWords, tweetlist):
        x = randrange(0,len(lastWords))
        reList = []
        with open('dpw.cd') as infile:
            for line in infile:
                line = line.strip().split('\\')
                reList.append(line[1])
        eList = []
        oList = []
        if lastWords[x] in reList:
            eList.append('\\' + lastWords[x] + '\\')

            oList.append(lastWords[x])
        else:
            return self.repeat(lastWords,tweetlist)
    
        if len(eList) == 0:
            return self.repeat(lastWords,tweetlist)
        else:
            self.getSound(eList, oList, tweetlist)

    def getSound(self, woord, oWoord, tweetlist):
        seen = set()
        seen_add = seen.add
        soundList = []
        with open('dpw.cd') as inf:
            for line in inf:
                if woord[0] in line:
                    line = line.strip().split('\\')
                    soundList.append(line[4] + '\\')
    
        var = [x for x in soundList if not (x in seen or seen_add(x))]

        ween= set()
        ween_add = ween.add
        rWordList = []
        with open('dpw.cd') as infi:
            for line in infi:
                if soundList[0] in line:
                    line = line.strip().split('\\')
                    rWordList.append(line[1])
        var1 = [y for y in rWordList if not (y in ween or ween_add(y))]
        self.compare(oWoord, var1, tweetlist)

    def compare(self, oWoord, rWoord, tweets):
        
        oList = []
        rList = []
        wasteList = []
        for line in tweets:
            if oWoord[0] in line:
                x = line.split()
                if x[-1] == oWoord[0]:
                    oList.append(line)
        
        for line in tweets:
            for i in rWoord:
                if i in line:
                    y = line.split()
                    if y[-1] == oWoord[0]:
                        wasteList.append(line)
                    elif y[-1] == i:
                        rList.append(line)
    

        if len(rList) > 0:
            self.initUI(oList,rList)
        else: self.getTweets()

def main():

    app = QtGui.QApplication(sys.argv)
    sc = Scherm()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
