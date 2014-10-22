def has_duplicates(lst):
	new=[]
	for element in lst:
		if element in new:
			return False
		else:
			new.append(element)
	return True


print has_duplicates([1,2,3,4,5,6,7])
print has_duplicates([1,2,3,2,5,6,7])
