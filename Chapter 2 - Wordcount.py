#This script ranks the words in "Tale of Two Cities" (Charles Dickens) descending by word count.
import collections

#Open and read the text file
file=open('98-0.txt')
file = file.read()

#Create a list of all words in the file.
list = file.split()

#Create a dictionary that keeps track of the wordcount
wordcount = {}
for word in list:
    word = word.lower()
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("\n", "")
    word = word.replace("“", "")
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1

#Create a ranking of the wordcounts and print the 10 most common words
d = collections.Counter(wordcount)
print(d.most_common(10))

#The code below does removes common stopwords from the dictionary.
stopwords = open("stopwords")
stopwords = stopwords.read()
stopwords = stopwords.split()
for i in stopwords:
    if i in wordcount:
            del wordcount[i]
d = collections.Counter(wordcount)
print(d.most_common(10))
