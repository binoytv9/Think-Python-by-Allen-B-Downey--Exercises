def reverse_pair(word_list):
	for word in word_list:
		if binary_search(word_list,word[::-1]):
			print word,word[::-1]


def binary_search(sorted_list,word):
	high=len(sorted_list)
	low=0

	while low < high:
		mid=(low+high)/2
		if word < sorted_list[mid]:
			high=mid
		elif word == sorted_list[mid]:
			return True
		else:
			low=mid+1
	return False

fin=open('words.txt').read().split()

reverse_pair(fin)
