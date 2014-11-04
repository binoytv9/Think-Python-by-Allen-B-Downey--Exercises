"""	Rewrite time_to_int (from "Prototyping Versus Planning" (page 184)) as a method. It
	is probably not appropriate to rewrite int_to_time as a method; what object you would
	invoke it on?	"""


class Time(object):
	""" time """
	def time_to_int(self):
		minutes=self.hour*60 + self.minute
		seconds=minutes*60 + self.second
		return seconds

	def increment(self,seconds):
		seconds+=self.time_to_int()
		return int_to_time(seconds)

	def print_time(self):
		print '\n%.2d:%.2d:%.2d\n' %(self.hour,self.minute,self.second)


def int_to_time(seconds):
	time=Time()
	time.minute,time.second = divmod(seconds,60)
	time.hour,time.minute = divmod(time.minute,60)
	return time


start=Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()
end=start.increment(1337)
end.print_time()
