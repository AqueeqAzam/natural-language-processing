import nltk
from nltk import sent_tokenize, word_tokenize

# sentences tokenizing
var = "Natural language processing, or NLP, combines computational linguistics—rule-based modeling of human language—with statistical. While machine learning models to enable computers and digital devices to recognize, understand and generate text and speech."
var

from nltk.tokenize import word_tokenize, sent_tokenize

sent = sent_tokenize(var)
sent

# with for loop
for i in sent:
  print(i)
  print()

word = word_tokenize(var)
word

# with importing files
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
