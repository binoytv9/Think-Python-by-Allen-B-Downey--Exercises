def is_sorted(lst):
	pre_element=lst[0]
	for element in lst[1:]:
		if element < pre_element:
			return False
		pre_element=element

	return True

print is_sorted([1,2,2])
print is_sorted(['b','a'])
