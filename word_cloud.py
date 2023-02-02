from wordcloud import WordCloud
import matplotlib.pyplot as plt

# generating the wordcloud
wordcloud = WordCloud().generate('text')

# plot the word cloud

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud)

# to remove the axis value
plt.axis('off')
plt.show()
