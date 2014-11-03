"""	Write a boolean function called is_after that takes two Time objects, t1 and t2 , and
	returns True if t1 follows t2 chronologically and False otherwise. Challenge: don't use
	an if statement	"""


class Time(object):
	""" represent time """

def is_after(t1,t2):
	return t1.hour<t2.hour or ((t1.hour == t2.hour) and (t1.minute<t2.minute)) or ((t1.minute<t2.minute)and (t1.second<t2.second))


t2=Time()
t2.hour=20
t2.minute=37
t2.second=15

t1=Time()
t1.hour=20
t1.minute=55
t1.second=10

print is_after(t1,t2)
