from nltk.corpus import stopwords

APPOSTROPHES = {
    "don't"   : "do not",
    "won't"   : "will not",
    "it's"    : "it is",
    "can't"   : "can not",
    "I'll"    : "I will",
    "I've"    : "I have",
    "you're"  : "you are",
    "didn't"  : "did not",
    "she's"   : "she is",
    "they're" : "they are",
    "we're"   : "we are",
    "you've"  : "you have",
    "aren't"  : "are not",
    "she'd"   : "she would",
    "he'd"    : "he would",
    "let's"   : "let us",
    "we've"   : "we have",
    "couldn't": "could not",
    "who's"   : "who is",
}

original_tweet = "I luv my &lt;3 iphone &amp; you're awsm apple. DisplayIsAwesome, sooo happppppy :) http://www.apple.com"

SLANGS = []

with open("slangwords.txt") as f:
    for line in f:
        slang, _ = line.split('\n')
        SLANGS.append(slang)

cachedStopWords = stopwords.words("english")