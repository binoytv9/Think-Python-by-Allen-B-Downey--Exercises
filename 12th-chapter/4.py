def anagrams(filename):
	wlist=get_wlist(filename)
	d={}
	for word in wlist:
		sword=''.join(sorted(word))
		d.setdefault(sword,[]).append(word)
	t=[]
	for key in d:
		if len(d[key])>1:
			t.append((len(d[key]),d[key]))
	t.sort(reverse=True)
	for l,lst in t:
		print lst


def get_wlist(filename):
	return open('words.txt').read().split()


anagrams('words.txt')
