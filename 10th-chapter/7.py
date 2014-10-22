def is_anagram(str1,str2):
	lst1=list(str1)
	lst2=list(str2)

	lst1.sort()
	lst2.sort()

	return lst1 == lst2

print is_anagram('eat','ate')
print is_anagram('binoy','yonib')
