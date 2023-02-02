"""from nltk.stem import PorterStemmer
porter = PorterStemmer()

# word list for stemming
word_list = ['study', 'studying', 'studies', 'studied']
# for w in word_list:
     # print(porter.stem(w))

from nltk.tokenize import word_tokenize
new_text = 'It is very important to learn python for neural network precessing'
words = word_tokenize(new_text)
for w in words:
    print(porter.stem(w))

from nltk.stem import SnowballStemmer

# print language supported
l = SnowballStemmer.languages
print(l)"""

from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
input_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize'
               'possibly', 'provision', 'hospital', 'kept', 'scratchy', 'code']

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

stemmer_names = ['PORTER', 'LANCASTER', 'SNOWBALL']
formatted_text = '{:>16}' * {len(stemmer_names) + 1}

print('\n', formatted_text.format('INPUT WORD', *stemmer_names),
'\n', '='*68)

