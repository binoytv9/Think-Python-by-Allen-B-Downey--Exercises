def uses_only(string,letters):
	wordlist=string.lower().split()
	letters=letters.lower()

	for word in wordlist:
		for wordletter in word:
			if wordletter not in letters:
				return False
	return True

print uses_only("Hoe alfalfa","acefhlo")
