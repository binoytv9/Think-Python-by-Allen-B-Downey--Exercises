def is_abecedarian(word):
	pre_letter=''
	for letter in word:
		if letter<pre_letter:
			return False
		pre_letter=letter
	return True

print is_abecedarian('binooy')
print is_abecedarian('bunoy')
print is_abecedarian('ABIL')
