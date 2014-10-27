def sort_by_random(words):
	t=[]
	for word in words:
		t.append((len(word),random.random,word))

	t.sort(reverse=True)

	res=[]
	for length,rnum,word in t:
		res.append(word)
	return res

import random
print sort_by_random(['asd','dfgd','erw','awer','asdsfd','sdfghf'])
