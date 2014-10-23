def reverse_lookup(d,v):
	k_list=[]
	for k in d:
		if d[k] == v:
			k_list.append(k)

	return k_list

print reverse_lookup({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1},1)
print reverse_lookup({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1},0)
