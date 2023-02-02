# Lemmatization tries to achieve a similar base “stem” for a word.
# However, what makes it different is that it finds the dictionary word instead of truncating the original word.

"""from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('studies'))
print(stemmer.stem('fucking'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('studies'))
print(lemmatizer.lemmatize('fucking'))

# a simpole demonstration of lemmanization
from nltk import WordNetLemmatizer
lemma = WordNetLemmatizer()
word_list = ['study', 'studying', 'studies', 'studied']
for w in word_list:
    print(lemma.lemmatize(w))"""


from nltk import WordNetLemmatizer
leema = WordNetLemmatizer()
word_list = ['studies', 'leaves', 'decrease', 'plays']

for w in word_list:
    print(leema.lemmatize(w))

