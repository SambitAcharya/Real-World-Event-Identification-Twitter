import re
import enchant
import HTMLParser

from constants import original_tweet
from constants import cachedStopWords
from itertools import groupby

def escapeHTMLChars(tweet):
    html_parser = HTMLParser.HTMLParser()
    tweet = html_parser.unescape(tweet)
    return tweet


def decodeData(tweet):
    tweet =  tweet.decode("utf8").encode('ascii','ignore')
    return tweet


def appostropheLookup(tweet):
    from constants import APPOSTROPHES
    words = tweet.split()
    reformed = [APPOSTROPHES[word] if word in APPOSTROPHES \
    else word for word in words]
    reformed = " ".join(reformed)
    return reformed


def removeEmoji(tweet):
    myre = re.compile(u'['
        u'\U0001F300-\U0001F64F'
        u'\U0001F680-\U0001F6FF'
        u'\u2600-\u26FF\u2700-\u27BF]+',
        re.UNICODE)

    tweet = myre.sub('', tweet)
    return tweet

def splitAttachedWords(tweet):
    tweet = " ".join(re.findall('[A-Z][^A-Z]*', tweet))
    return tweet


def standardizeWords(tweet):
    tweet = ''.join(''.join(s)[:2] for _, s in groupby(tweet))
    return tweet


def removeLinks(tweet):
    links_re = re.compile("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)")
    tweet = links_re.sub(" ",tweet)
    tweet = ' '.join(tweet.split())
    return tweet


def removeSlangs(tweet):
    from constants import SLANGS
    words = tweet.split()
    reformed = [' ' if word in SLANGS else word for word in words ]
    reformed = " ".join(reformed)
    return reformed


def removeShortTweets(tweet):
    words = tweet.split()
    if len(words)<3:
        return ''
    else:
        return tweet


def removeStopWords(tweet):
    words = tweet.split()
    reformed = [word for word in tweet.split() if word not in cachedStopWords]
    return " ".join(reformed)

def removeNonEnglishTweets(tweet):
    words = tweet.split()
    d = enchant.Dict("en_US")
    count = 0
    total = len(words)
    if total == 0:
        return ''
    # print total
    for word in words:
        if not d.check(word):
            count += 1
    # print count
    percentage = float(count)/total * 100
    # print percentage
    if percentage >= 60:
        return ''
    else:
        return tweet


def cleanTweet(tweet):
    clean_tweet = tweet

    clean_tweet = escapeHTMLChars(clean_tweet)
    clean_tweet = decodeData(clean_tweet)
    clean_tweet = appostropheLookup(clean_tweet)
    clean_tweet = removeEmoji(clean_tweet)
    clean_tweet = removeStopWords(clean_tweet)
    clean_tweet = standardizeWords(clean_tweet)
    clean_tweet = removeLinks(clean_tweet)
    clean_tweet = removeSlangs(clean_tweet)
    clean_tweet = removeShortTweets(clean_tweet)
    clean_tweet = removeNonEnglishTweets(clean_tweet)

    return clean_tweet
