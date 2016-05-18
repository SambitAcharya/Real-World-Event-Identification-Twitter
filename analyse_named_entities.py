def get_words_with_entities(batchfile):
    '''
        Function to get all the words in all the tweets
        along with the entity for the word.
    '''

    entities = []

    with open(batchfile) as file:
        for line in file:
            entities.append(line)

    word_entity_list = []
    for entity in entities:
        word_entity_list.append(entity.split())

    word_entity_list = word_entity_list[:-1]
    word_entities = []

    for word in word_entity_list:
        for k in word:
            word_entities.append(k.split('/'))

    return word_entities


def get_important_words(batchfile):
    '''
        Function to get all the important words which can
        indicate specific events
    '''

    important_words = []
    word_entities = get_words_with_entities(batchfile)
    for word_entity in word_entities:
        if word_entity[-1]!='O':
            word = word_entity[0]
            important_words.append(word)


    return important_words


# important_words = get_important_words()
# print important_words
