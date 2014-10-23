def word_dict(filename):
	word_list=open(filename).read().split()
	d={}
	for word in word_list:
		d[word] = 1
	return d


def rotate_word(word,i):
	rword=''
	l=len(word)
	for index in range(l):
		rword+=word[(index+i)%l]
	return rword


def rotate_pair(filename):
	wdict=word_dict(filename)
	for word in wdict:
		for i in range(1,len(word)):
			rword=rotate_word(word,i)
			if rword in wdict:
				print word,rword

rotate_pair('words.txt')
