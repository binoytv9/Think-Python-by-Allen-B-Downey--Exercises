def check3consecutive_double_letter(word):
	pre_letter=''
	index=0
	count=0

	while index < len(word):
		if word[index] == pre_letter:
			count+=1
			if count == 3:
				return True
			index+=2
			if index >= len(word):
				break
			pre_letter=word[index-1]
		else:
			pre_letter = word[index]
			index+=1
			count=0
	return False

def display(filename):
	wordlist=open(filename).read().split()
	for word in wordlist:
		if check3consecutive_double_letter(word):
			print word

display('words.txt')
