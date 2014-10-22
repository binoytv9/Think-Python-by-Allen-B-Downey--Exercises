def count(word,char):
	count = 0
	index=0
	while True:
		ind = find(word,char,index)
		if ind >= 0 :
			count = count + 1
			index=ind+1
		else:
			break
	print count

def find(word,letter,index):
	while index<len(word):
		if word[index] == letter:
			return index
		index+=1
	return -1

count("binoy","i")
count("abacad","a")
