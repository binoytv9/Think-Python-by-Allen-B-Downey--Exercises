def to_lower(words):
	for index in range(len(words)):
		words[index]=words[index].lower()


def word_count(words):
	d={}
	for word in words:
		d[word]=d.get(word,0) + 1
	return d


def rem_specialchar(words):
	for index in range(len(words)):
		words[index]=words[index].translate(None,string.punctuation)


def printfreq(d):
	for word,count in d.items():
		print word,count


import string
wlist=open('book.txt').read().split()
to_lower(wlist)
rem_specialchar(wlist)
wdict=word_count(wlist)
printfreq(wdict)
