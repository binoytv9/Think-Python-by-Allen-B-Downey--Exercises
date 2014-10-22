def is_palindrome(string):
	return string == string[::-1]

def sixdigitnumber():
	lst=[]
	for sixdigitnum in range(100000,1000000):
		lst.append(str(sixdigitnum))
	return lst

def check_cond(num):
	if is_palindrome(num[-4:]):
		intnum=string.atoi(num) + 1
		num=str(intnum)

		if(is_palindrome(num[-5:])):
			intnum=string.atoi(num) + 1
			num=str(intnum)

			if(is_palindrome(num[1:-1])):
				intnum=string.atoi(num) + 1
				num=str(intnum)

				if(is_palindrome(num)):
					return True
	return False


def display():
	for num in sixdigitnumber():
		if check_cond(num):
			print num

import string
display()
