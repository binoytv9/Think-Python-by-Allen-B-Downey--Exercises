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


def printfreq(t,num=20):
	for word,count in t[:num]:
		print word,count


def to_tuple(d):
	t=[]
	for word,count in d.items():
		t.append((count,word))
	return t


import string
wlist=open('book.txt').read().split()
to_lower(wlist)
rem_specialchar(wlist)
wdict=word_count(wlist)
wtuple=to_tuple(wdict)
wtuple.sort(reverse=True)
printfreq(wtuple)
