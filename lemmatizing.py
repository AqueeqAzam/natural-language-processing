# Lemmatization tries to achieve a similar base “stem” for a word.
# However, what makes it different is that it finds the dictionary word instead of truncating the original word.
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

w1 = WordNetLemmatizer()
w1.lemmatize('mice')


