import string
import subprocess
import fileinput
import re
from random import randrange



def getTweets():
    tweets = []
    with open('gestolentweets.txt') as infile:
        for line in infile:
            removeUrl = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', line)
            tweets.append(removeUrl)
    return tweets

def getLastWord(tweetlist):
    lastWords = [item.split()[-1] for item in tweetlist]
    lastWords = [''.join(c for c in s if c not in string.punctuation) for s in lastWords]
    lastWords = [x for x in lastWords if x]
    reList = []
    with open('dpw.cd') as infile:
        for line in infile:
            line = line.strip().split('\\')
            reList.append(line[1])
    woord, oWoord = repeat(lastWords, reList)

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

    return oWoord, var1
    
def repeat(lastWords, reList):
    x = randrange(0,len(lastWords))
    eList = []
    oList = []
    if lastWords[x] in reList:
        eList.append('\\' + lastWords[x] + '\\')
        oList.append(lastWords[x])
    else:
        return repeat(lastWords, reList)

    if len(eList) == 0:
        return repeat(lastWords, reList)
    else:
        return eList, oList

def compare(oWoord, rWoord, tweets):
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
        print(oList[0], rList[0])
    else: print("Geen tweets gevonden")
        
def main():
    x = getTweets()
    z,y= getLastWord(x)
    compare(z, y, x)

if __name__ == "__main__":
    main()
