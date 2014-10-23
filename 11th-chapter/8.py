def  rsa():

	print '\n\nSelect two distinct prime numbers...'
	p=random_prime(10)
	print '\n\t\tp = ',p
	q=random_prime(p)
	print '\t\tq = ',q

	print '\nCompute n = pq'
	n=p*q
	print '\t\tn = ',n

	print "\n\nCompute Phi(n) = (p-1)(q-1)"
	t=(p-1)*(q-1)
	print '\t\tPhi(n) = ',t

	print '\n\nChoose an integer e such that 1 < e < Phi(n) and gcd(e, Phi(n)) = 1; i.e., e and Phi(n) are coprime. '
	e=random_prime(t)
	print '\t\te = ',e

	print '\n\nDetermine d as d = e^-1 (mod Phi(n))'
	d=mod_mul_inv(e,t)
	print '\t\td = ',d

	print '\n\npublic key : (%d,%d)' %(n,e)
	print '\n\nprivate key : (%d,%d)' %(n,d)
	m=int(raw_input("\n\nenter the message : "))

	c=mod_exp(m,e,n)
	print '\n\n\t\tencrypted message is ',c

	m=mod_exp(c,d,n)
	print '\n\n\t\tdecrypted message is ',m
	print '\n\n'


def mod_exp(m,e,n):
	c=1
	e1=0

	while e1<e:
		e1+=1
		c=(m*c)%n

	return c


def random_prime(p=None):
	while True:
		num=random.randint(10,100)
		if is_prime(num):
			if p!=None and p%num != 0:
				return num

def is_prime(num):
	for i in range(2,num/2+1):
		if num%i == 0:
			return False
	return True

def mod_mul_inv(e,t):
	for d in range(1,t):
		if (e*d) % t == 1:
			return d

import random
rsa()
