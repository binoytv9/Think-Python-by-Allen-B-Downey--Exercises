"""	Rewrite increment using time_to_int and int_to_time	"""


class Time(object):
	""" time """

def time_to_int(t):
	minute = t.hour*60 + t.minute
	second = minute*60 + t.second
	return second


def int_to_time(second):
	t=Time()
	t.minute,t.second = divmod(second,60)
	t.hour,t.minute = divmod(t.minute,60)
	return t


def increment(time,second):
	seconds=time_to_int(time)
	return int_to_time(seconds+second)	
