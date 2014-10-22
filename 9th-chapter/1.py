def word20char(filename):
	fin=open(filename)
	for line in fin:
		word=line.strip()
		if len(word)>20:
			print word


word20char('a.txt')
