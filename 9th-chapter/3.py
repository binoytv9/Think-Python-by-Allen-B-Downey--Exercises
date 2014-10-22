def avoids(words,forbiddenletters):
	for word in words:
		k=1
		for forbiddenletter in forbiddenletters:
			if forbiddenletter in word:
				k=0
				break
		if k==1:
			print word,

forbiddenletters = raw_input("\n\nenter the forbidden letters : ");
words=open('words.txt').readlines()

avoids(words,forbiddenletters)
