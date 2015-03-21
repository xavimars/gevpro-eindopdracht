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
    

def main():
    x = getTweets()
    getLastWord(x)
    


if __name__ == "__main__":
    main()
