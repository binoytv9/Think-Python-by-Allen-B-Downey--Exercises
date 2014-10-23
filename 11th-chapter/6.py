def fib_dict(n):
	if n in known:
		return known[n]

	res=fib_dict(n-1) + fib_dict(n-2)
	known[n]=res

	return res

def fib(n):
	if n<2:
		return n
	return fib(n-1) + fib(n-2)

import time
known={0:0,1:1}
m=40

start=time.time()
print fib_dict(m)
stop=time.time()
print stop-start

start=time.time()
print fib(m)
stop=time.time()
print stop-start
