def children(word):
	t=[]
	for i in range(len(word)):
		cword=child(word,i)
		if cword in dwords:
			t.append(cword)
	return t


def child(word,index):
	new=''
	for i in range(len(word)):
		if i == index:
			continue
		new+=word[i]
	return new


def word_dict(filename):
	d={}
	wlist=open(filename).read().split()
	for word in wlist:
		d[word]=1
	d['']=1
	return d

def main():
	for word in dwords:
		reducible(word,[])


def reducible(word,lst):
	if word == '':
		rwlist.append((len(lst),lst[:]))
		return
	lst.append(word)
	for i in children(word):
		reducible(i,lst[:])



def longst(d):
	l=d[0][0]
	print 'length is ',l
	for t in d:
		if t[0]<l:
			return
		print t[1]
		print

rwlist=[]
dwords=word_dict('words.txt')
main()
rwlist.sort(reverse=True)
longst(rwlist)
