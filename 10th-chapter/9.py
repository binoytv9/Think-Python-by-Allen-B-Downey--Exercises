def remove_duplicates(lst):
	new=[]
	for element in lst:
		if element not in new:
			new.append(element)
	return new

print remove_duplicates([1,2,3,4,5,6])
print remove_duplicates([1,2,2,4,6,6])
