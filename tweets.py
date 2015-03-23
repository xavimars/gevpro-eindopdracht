import string


# De tweets in sample.txt format krijgen doen we met command line argumenten naar
# een text bestand.

def getTweets():
    tweets = []
    with open('sample.txt') as infile:
        for line in infile:
            tweets.append(line)
    return tweets

def getLastWord(tweetlist):
    lastWords = [item.split()[-1] for item in tweetlist]
    lastWords = [''.join(c for c in s if c not in string.punctuation) for s in lastWords]
    print(lastWords)

def compare(lastWord, searchSound):
    eList = []
    for i in lastWord:
        for o in searchSound:
            if i == o:
                eList.append(i)



def searchWord(lastWords):
    reList = []
    with open('dpw.cd') as infile:
        for line in infile:
            line = line.strip().split('\\')
            reList.append(line[1])
    return reList      


def main():
    x = getTweets()
    lw = getLastWord(x)
    sw = searchWord(lw)
    c = compare(lw,sw)

if __name__ == "__main__":
    main()
