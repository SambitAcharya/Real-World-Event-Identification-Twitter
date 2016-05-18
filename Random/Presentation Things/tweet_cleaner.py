import re
import enchant
import HTMLParser

from constants import original_tweet
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
    tweet = " ".join(re.findall('[A-Z][^A-Z]*', original_tweet))
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
    reformed = ['*'*len(word) if word in SLANGS else word for word in words ]
    reformed = " ".join(reformed)
    return reformed


def removeShortTweets(tweet):
    words = tweet.split()
    if len(words)<5:
        return ''
    else:
        return tweet


def removeNonEnglishTweets(tweet):
    words = tweet.split()
    d = enchant.Dict("en_US")
    flag = 0
    for word in words:
        if not d.check(word):
            flag = 1
            break

    if flag:
        return ''
    else
        return tweet
