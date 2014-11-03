"""	Write a "pure" version of increment that creates and returns a new Time object rather
	than modifying the parameter	"""


class Time(object):
	""" time """


def increment(t,seconds):
	time=copy.deepcopy(t)
	time.second+=seconds

	if time.second>=60:
		time.minute += time.second/60
		time.second %= 60

	if time.minute>=60:
		time.hour += time.minute/60
		time.minute %= 60

	return time


import copy

t=Time()
t.hour=5
t.minute=56
t.second=58

s=260

nt=increment(t,s)
print '\nold\n\n\t%.2d:%.2d:%.2d\n' %(t.hour,t.minute,t.second)
print '\nnew after adding %d seconds\n\n\t%.2d:%.2d:%.2d\n' %(s,nt.hour,nt.minute,nt.second)
