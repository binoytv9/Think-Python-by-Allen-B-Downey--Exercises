"""	Write a correct version of increment that doesn't contain any loops	"""


class Time(object):
	""" time """


def increment(time,seconds):
	time.second+=seconds

	if time.second>=60:
		time.minute += time.second/60
		time.second %= 60

	if time.minute>=60:
		time.hour += time.minute/60
		time.minute %= 60


t=Time()
t.hour=5
t.minute=56
t.second=58

s=260

print '\nbefore\n\n\t%.2d:%.2d:%.2d\n' %(t.hour,t.minute,t.second)
increment(t,s)
print '\nafter adding %d seconds\n\n\t%.2d:%.2d:%.2d\n' %(s,t.hour,t.minute,t.second)
