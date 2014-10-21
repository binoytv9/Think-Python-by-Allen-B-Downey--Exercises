def is_palindrome(word):
	if len(word)<=1:
		return True

	if first(word) != last(word):
		return False

	else:
		return is_palindrome(middle(word))

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

print is_palindrome("binoy")
print is_palindrome("b")
print is_palindrome("noon")
