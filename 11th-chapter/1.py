def keyz(filename):
	word_list=open(filename).read().split()

	i=0
	word_dict={}
	for word in word_list:
		word_dict[word]=i
		i+=1

	return word_dict

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

import time
word_list=open('words.txt').read().split()
w=keyz('words.txt')

print 'dictionary in'
start=time.time()
print start
print 'jawbone' in w
stop=time.time()
print stop
print stop-start

print '\nlist in'
start=time.time()
print start
print 'jawbone' in word_list
stop=time.time()
print stop
print stop-start

print '\nbinary search'
start=time.time()
print start
print binary_search(word_list,'jawbone')
stop=time.time()
print stop
print stop-start
