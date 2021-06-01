import re
from caesar_cipher.corpus_loader import word_list, name_list

def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count


def is_english_word(text : str):
    word_count = count_words(text)
    percentage = int(word_count / len(text.split()) * 100)
    return percentage

import re


def gg():
    return