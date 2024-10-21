import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

res= urllib.request.urlopen('https://en.wikipedia.org/wiki/Vijay_(actor)')
html= res.read()

##print(html)

soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip = True)

#print(text)

tokens = [t for t in text.split()]


sr= stopwords.words('english')
clean_token= tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_token.remove(token)

#print(clean_token)

fre= nltk.FreqDist(clean_token)
for key,val in fre.items():
    print(str(key) + ":" + str(val))
fre.plot(20)


