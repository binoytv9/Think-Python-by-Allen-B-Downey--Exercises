def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def capitalize_nested(nested_list):
	new=[]
	for list in nested_list:
		new.append(capitalize_all(list))

	return new

print capitalize_nested([['asd','et'],['tyt','jku','qwe']])
	
