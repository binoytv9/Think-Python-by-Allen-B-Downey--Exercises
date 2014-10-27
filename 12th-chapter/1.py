def sumall(*n):
	s=0
	for i in n:
		s+=i
	return s

print sumall(1,2,3,4)
print sumall(*[1,2,3,4])
