def binary_search(sorted_list,word):
	high=len(sorted_list)
	low=0

	while low < high:
		mid=(low+high)/2
		if word < sorted_list[mid]:
			high=mid
		elif word == sorted_list[mid]:
			return mid
		else:
			low=mid+1
	return None

fin=open('words.txt').read().split()

print binary_search(fin,'zymurgy')
