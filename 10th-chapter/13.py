def find_interlock_words(word_list):
	for index1 in range(len(word_list)):
		for index2 in range(len(word_list)):
			if len(word_list[index1])==len(word_list[index2]) and binary_search(word_list,interlock(word_list[index1],word_list[index2])):
				print word_list[index1],word_list[index2]


def interlock(w1,w2):
	new=''
	j=k=0
	for i in range(2*len(w1)):
		if i%2==0:
			new+=w1[j]
			j+=1
		else:
			new+=w2[k]
			k+=1
	return new


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
find_interlock_words(fin)
