"""importing required libarary
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

# sentences tokenizing
# import file
text_file = open('/home/tyson/typing practices.txt')

# Read the data
text = text_file.read()

# Tokenize the text by sentence
sentences = sent_tokenize(text)

# how many sentences are there
# print(len(sentences))
# print(sentences)

# word tokenization
words = word_tokenize(text)
# print(len(words))
# print(words)


# frequency distribution
from nltk.probability import FreqDist
# find the frequency
fdisk = FreqDist(words)

fdisk.most_common(10)
print(fdisk)

# plot the frequency graph
import matplotlib.pyplot as plt
# fdisk.plot(10)

# Remove punctuation marks
# empty list to store words
words_no_punc = []

# Remove punctuaton marks
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

# print the words without puncuation marks
# print(words_no_punc)
# print('\n')
# length
# print(len(words_no_punc))

# list od stop words

from nltk.corpus import stopwords

# list of stopwords
stopwords = stopwords.words('english')
# print(stopwords)
# empty list to clean words

clean_words = []
for w in words_no_punc:
    if w not in clean_words:
        clean_words.append(w)
print(clean_words)
print('\n')
print(len(clean_words))

fdist = FreqDist(clean_words)
fdist.most_common(10)
fdist.plot(10)"""

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

text_file = open('/home/tyson/typing practices.txt')
text = text_file.read()
# print(text)

sen = sent_tokenize(text)
# print(sen)
# print(len(sen))

words = word_tokenize(text)
# print(words)
# print(len(words))

from nltk.probability import FreqDist
fdisk = FreqDist(words)
fdisk.most_common(10)
# print(fdisk)

import matplotlib.pyplot as plt
# fdisk.plot(10)

words_of_punc = []
for w in words_of_punc:
    if w.isaplha():
        words_of_punc.append(w.lower())
print(words_of_punc)


