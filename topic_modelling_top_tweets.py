from collections import Counter
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel

from itertools import izip
from collections import defaultdict
from pprint import pprint

def get_corpus(documents):
    texts = [ [word for word in document.lower().split()]
            for document in documents]

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1]
            for text in texts]

    dictionary = corpora.Dictionary(texts)
    dictionary.save('/tmp/mytopicmodellingdicti.dict')


    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('/tmp/mytopicmodellingdicti.mm', corpus)
    return corpus, dictionary


top_tweets = []
with open('cleaned_tweets_file.txt') as tweets:
    for tweet in tweets:
        if "Kobe" in tweet:
            top_tweets.append(tweet.rstrip('\n'))

corpus, dictionary = get_corpus(top_tweets)
corpus_tfidf = models.TfidfModel(corpus)

for k in range(5,28,3):
    print "Number of topics ", k
    lda = ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=k)
    corpus_lda = lda[corpus]

    events = []
    for i in range(lda.num_topics):
        topic_string = str(lda.print_topic(i))
        topics = topic_string.split('+')
        percentage_dict = {}
        for topic in topics:
            percentage,event = topic.split('*')
            if event in percentage_dict:
                percentage_dict["event"] += percentage
            else:
                percentage_dict["event"] = percentage
            events.append(event)
    counts = dict(Counter(events)).items()
    # for count in counts:
    #     count[1] *= percentage_dict[count[0]]
    # print counts
    counts = sorted(counts, key = lambda k:k[1], reverse=True)
    main_event = []
    for count in counts:
        if count[1]>(k/3):
            if (count[0] != 'sports ' and len(count[0]) > 3):
                # print len(count[0])
                main_event.append(count[0])
    print ''.join(main_event)
