def invert_dict(d):
	inv={}
	for k in d:
		inv.setdefault(d[k],[]).append(k)
	return inv

print invert_dict({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1})
