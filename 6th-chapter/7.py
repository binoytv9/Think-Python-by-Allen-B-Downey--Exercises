def is_power(a,b):
	if b == 0:
		print "integer division or modulo by zero!!!"
		return None

	if a==0:
		return True

	if a%b == 0:
		return is_power(a/b,b)
	else:
		return False

print
print is_power(1,2)
print
print is_power(0,2)
print
print is_power(1,0)
print
