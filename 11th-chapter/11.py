def homophone(filename):
	wlist=open(filename).read().split()
	d=pronounce.read_dictionary('c06d')

	for word in wlist:
		if len(word) == 5 and word in d:
			mword=modify(word,0)
			if mword in d and d[mword] == d[word]:
				mword=modify(word,1)
				if mword in d and d[mword] == d[word]:
					print word


def modify(word,i):
	new=''
	for index in range(len(word)):
		if index == i:
			continue
		new+=word[index]
	return new

import pronounce

homophone('words.txt')
