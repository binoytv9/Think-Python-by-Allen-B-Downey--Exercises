def to_dict(words):
	d={}
	for word in words:
		d[word]=1
	return d


def rem_specialchar(wl):
	for index in range(len(wl)):
		wl[index]=wl[index].translate(None,string.punctuation)



def printdiff(bd,wd):
	for bword in bd:
		if bword not in wd:
			print bword


import string
wlist=open('words.txt').read().split()
rem_specialchar(wlist)
wdict=to_dict(wlist)

blist=open('book.txt').read().split()
rem_specialchar(blist)
bdict=to_dict(blist)

printdiff(bdict,wdict)
