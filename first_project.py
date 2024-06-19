x = "Natural language processing, or NLP, combines computational linguistics—rule-based modeling of human language—with statistical and machine learning models to enable computers and digital devices to recognize, understand and generate text and speech."

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# seperate the word
w = word_tokenize(x)
w

from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
# check part of speech
p = pos_tag(w)
p
