import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize
text = " Hellow World! How are You ?"
words = word_tokenize(text)
print(words)