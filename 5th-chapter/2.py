"""	Write a function called do_n that takes a function object and a number, n , as arguments,
and that calls the given function n times.	"""

def do_n(f,n):
	if n<=0:
		return

	f()
	do_n(f,n-1)

do_n(foo,3)
