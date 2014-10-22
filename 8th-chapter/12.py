def rotate_word(word,num):
	new=''
	for letter in word:
		if letter.isupper():
			ordr=ord(letter)+num
			if ordr > 90:
				new+=chr(ordr-26)
			elif ordr < 65:
				new+=chr(ordr+26)
			else:
				new+=chr(ordr)
		elif letter.islower():
			ordr=ord(letter)+num
			if ordr > 122:
				new+=chr(ordr-26)
			elif ordr < 97:
				new+=chr(ordr+26)
			else:
				new+=chr(ordr)
		else:
			print '\n\n\tinvalid word\n\n'
			return None

	return new

print rotate_word('binoy',3)
print rotate_word('cheer',7)
print rotate_word('melon',-10)
