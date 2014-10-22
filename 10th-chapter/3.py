def cumulative_sum(num_list):
	new=[]
	sum=0

	for num in num_list:
		sum+=num
		new.append(sum)
	return new

print cumulative_sum([1,2,3])
