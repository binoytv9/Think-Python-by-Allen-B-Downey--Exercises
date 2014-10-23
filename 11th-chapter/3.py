def print_hist(dictionary):
	key_list=dictionary.keys()
	key_list.sort()

	for key in key_list:
		print key,dictionary[key]


print_hist({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1})
