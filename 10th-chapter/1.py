def nested_sum(nested_list):
	sum=0
	for list in nested_list:
		for element in list:
			sum+=element
	return sum

print nested_sum([[1,2,4],[5,6,7],[4,5,3]])
