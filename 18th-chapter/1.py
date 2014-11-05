"""	Write a __cmp__ method for Time objects	"""


class Time(object):
	""" represent a time object """
	def __init__(self,hour=0,minute=0,second=0):
		self.hour=hour
		self.minute=minute
		self.second=second


	def __str__(self):
		return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)
	def __cmp__(self,other):
		t1=self.hour,self.minute,self.second
		t2=other.hour,other.minute,other.second
		return cmp(t1,t2)


t1=Time(12,12,45)
print t1
t2=Time(2,12,10)
print t2
t3=Time(12,12,10)
print t3

print t1>t2
print t1>t3
