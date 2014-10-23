def histogram(word):
	d={}
	for letter in word:
		d[letter] = d.get(letter,0) + 1

	return d

print histogram('brontosaurus')
