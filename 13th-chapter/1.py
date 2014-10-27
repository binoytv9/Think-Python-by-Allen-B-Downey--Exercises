import string

wlist=open('a.txt').read().split()
newlist=[]
for word in wlist:
	newlist.append(word.translate(None,string.punctuation))
print ' '.join(newlist)
