import anagram_sets
import shelve

def store_anagrams():
	db=shelve.open('shelf','c')
	d=anagram_sets.all_anagrams('words.txt')
	for key in d:
		if len(d[key])>1:
			db[key]=d[key]
	db.close()


def read_anagrams(word):
	db=shelve.open('shelf')
	sword=''.join(sorted(word))
	if sword in db:
		return db[sword]
	else:
		return "\n\t'%s' not found\n" %word
