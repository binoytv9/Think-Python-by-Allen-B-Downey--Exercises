"""	Write a function called print_time that takes a Time object and prints it in the form
	hour:minute:second	"""


class Time(object):
	""" represent time of day """

def print_time(t):
	print '%.2d:%.2d:%.2d' %(t.hour,t.minute,t.second)


time=Time()
time.hour=11
time.minute=59
time.second=3

print_time(time)
