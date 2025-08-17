from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt_tab')


url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.summary
print(text)



blob = TextBlob(text)#just passing the string not the article object.
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)