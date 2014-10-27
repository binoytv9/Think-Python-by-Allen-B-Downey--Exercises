def to_set(words):
	s=set()
	for word in words:
		s.add(word)
	return s


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
wset=to_set(wlist)

blist=open('book.txt').read().split()
rem_specialchar(blist)
bset=to_set(blist)

print bset.difference(wset)
