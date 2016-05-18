from tweet_cleaner import cleanTweet

original_tweets = set()

with open('streamed_tweets.txt') as tweets:
	for count,tweet in enumerate(tweets):
		cleaned_tweet = cleanTweet(tweet)
		if cleaned_tweet not in original_tweets:
			original_tweets.add(cleaned_tweet)
			with open("cleaned_tweets_file.txt", "a") as f2:
				if cleaned_tweet:
					f2.write(cleaned_tweet+'\n')
				print 'Done ' + str(count+1)