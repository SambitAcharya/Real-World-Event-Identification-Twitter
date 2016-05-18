import httplib
import json
import sys

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'm4hn1XhwRIwxymXWXjNInKK9n'
csecret = 'GTsxprBuOpfrtx985PelmyXyJseQxpS2dge5neGvxSoO09D2ei'
atoken = '2365425174-5KtFxyQSCp9NPvJoyXLXXZQyhJg6qWtBMxtypGX'
asecret = 'Q2BCdRYyIRq37xA1llOq9YkvhZajSgvaVFMIjGuj3pciL'

class listener(StreamListener):

    def on_data(self, data):
        c = json.loads(data)
        tweet_text = c.get("text",None)
        print tweet_text
        with open("streamed_tweets.txt", "a") as f:
            try:
                if(tweet_text):
	               f.write(tweet_text)
	               f.write("\n")
            except httplib.IncompleteRead, e:
                page = e.partial
            except:
               print "Couldn't write tweet to file."

        return True


    def on_error(self, status_code):
        print "Encountered error with status code: ",status_code

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["sports", "cricket"])
# Filtering for tweets only in India
# twitterStream.filter(locations=[8.06, 68.17, 37.1, 97.41])
# twitterStream.filter(locations=[17.38,78.5,18.2,80])
