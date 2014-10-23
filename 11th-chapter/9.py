def has_duplicates(lst):
	d={}
	for element in lst:
		if element in d:
			return True
		d[element]=1
	return False


print has_duplicates([1,2,3,4,5])
print has_duplicates([1,2,3,3,5])
