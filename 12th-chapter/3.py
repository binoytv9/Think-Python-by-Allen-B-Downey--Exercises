def most_frequent(string):
	t=maketuple(string)
	t.sort(key=lambda x : x[1],reverse=True)

	for letter,count in t:
		print letter,'\t',count


def maketuple(string):
	d={}
	for letter in string:
		d[letter] = d.get(letter,0) + 1
	return d.items()

most_frequent(''.join(open('words.txt').read().split()))
