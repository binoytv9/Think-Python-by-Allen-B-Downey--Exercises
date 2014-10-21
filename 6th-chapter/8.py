def gcd(a,b):
	if a%b == 0:
		return b
	else:
		return gcd(b,a%b)

print gcd(15,10)
print gcd(10,15)
print gcd(1,2)
