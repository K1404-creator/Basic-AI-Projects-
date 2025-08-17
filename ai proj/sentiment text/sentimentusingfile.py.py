from textblob import TextBlob

#To analyze the text from the text file.
with open('mytext1.txt', 'r') as file:
    text = file.read()
blob = TextBlob(text)    
sentiment = blob.sentiment.polarity
print(sentiment)