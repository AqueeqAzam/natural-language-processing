from nltk.stem import LancasterStemmer, RegexpStemmer, PorterStemmer, SnowballStemmer

l = LancasterStemmer()
r = RegexpStemmer('ing')
p = PorterStemmer()
s = SnowballStemmer("english")

l.stem('charging')

r.stem('buying')

p.stem('fucking')

s.stem('cried')
