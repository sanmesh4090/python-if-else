from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "runner", "ran", "runs"]
stemmed_words = [ps.stem(word) for word in words]
print(stemmed_words)
