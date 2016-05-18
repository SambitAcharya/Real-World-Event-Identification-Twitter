import os
import pickle

from collections import Counter
from glob import glob
from heapq import nlargest

from analyse_named_entities import get_important_words

def tokenize_lines(line):
    words = line.split()
    return words


def get_batch_words_count(batch_path):

    words = get_important_words(batch_path)
    batch_counts = dict(Counter(words))
    return batch_counts


def get_total_words_count(total_words_counts, batch_path):
    batch_counts = get_batch_words_count(batch_path)

    for key,value in batch_counts.items():
        if key in total_words_counts:
            total_words_counts[key]+=batch_counts[key]
        else:
            total_words_counts[key]=batch_counts[key]

    return total_words_counts


def main():

    batch_paths = glob('tweets_batches/Batch_*')
    if os.path.isfile('counts.pickle'):
        os.remove('counts.pickle')

    for batch_path in batch_paths:
        try:
            with open('counts.pickle', 'rb') as handle:
                total_words_counts = pickle.load(handle)
        except IOError:
            total_words_counts = {}

        total_words_counts = get_total_words_count(total_words_counts, batch_path)
        total_words_counts["cricket"] = 0
        total_words_counts["Cricket"] = 0
        top_word_counts = nlargest(15, total_words_counts.items(), key=lambda k:k[1])
        top_words = [top_word_count[0] for top_word_count in top_word_counts]

        for top_word in top_words:
            category_list = ['cricket','sports']
            word_lower = top_word.lower()
            if word_lower in category_list:
                top_words.remove(top_word)

        for top_word in top_words:
            print top_word, total_words_counts[top_word]

        print "Batch Ends"
        print "----------------------------------"
        with open('counts.pickle', 'wb') as handle:
            pickle.dump(total_words_counts, handle)


if __name__ == '__main__':
    main()
