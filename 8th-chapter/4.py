def find(word,letter,index):
	while index<len(word):
		if word[index] == letter:
			return index
		index+=1
	return -1

print find('binoy','n',3)
