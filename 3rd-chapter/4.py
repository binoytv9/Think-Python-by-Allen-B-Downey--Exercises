def do_twice(f,val):
	f(val)
	f(val)

def print_twice(string):
	print string

def do_four(f,val):
	f(print_twice,val)
	f(print_twice,val)

do_four(do_twice,'spam')
