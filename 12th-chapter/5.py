def metathesis_pair(filename):
	wlist=getlist(filename)
	anagrams=anagram_tuple(wlist)
	for anagram in anagrams:
		for i in range(len(anagram)-1):
			 for j in range(i+1,len(anagram)):
				if diff_is_2(anagram[i],anagram[j]):
					print anagram[i],anagram[j]


def diff_is_2(w1,w2):
	count=0
	for i,j in zip(w1,w2):
			if i!=j:
				count+=1
	if count==2:
		return True
	else:
		return False


def anagram_tuple(wlist):
	d={}
	for word in wlist:
		sword=''.join(sorted(word))
		d.setdefault(sword,[]).append(word)

	t=[]
	for key in d:
		if len(d[key])>1:
			t.append(d[key])
	return t			


def getlist(filename):
	return open(filename).read().split()


metathesis_pair('words.txt')
