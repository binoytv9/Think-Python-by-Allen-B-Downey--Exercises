def square_root(a):
	x=a-1
	while True:
		y=(x+a/x)/2

		if abs(x-y) < epsilon:
			print x
			break

		x=y

epsilon=0.000000000001
print
square_root(5)
print
square_root(0)
print
square_root(9)
print
square_root(12.23)
print
