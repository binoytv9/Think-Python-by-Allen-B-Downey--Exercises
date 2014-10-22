def count(word,char):
	count = 0
	for letter in word:
		if letter == char:
			count = count + 1
	print count

count("binoy","i")
count("binoy","a")
