file_count = 1
with open('cleaned_tweets_with_entities.txt','r') as cleaned_tweets:
	for tweet_count, cleaned_tweet in enumerate(cleaned_tweets):
		if tweet_count % 1000 != 0:
			with open(file_name,'a') as f:
				f.write(cleaned_tweet)
		else:
			file_name = "Batch_" + str(file_count) + ".txt"
			file_count += 1