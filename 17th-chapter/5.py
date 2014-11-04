"""	Write an add method for Points that works with either a Point object or a tuple	"""


class Point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __add__(self,other):
		if isinstance(other,Point):
			return self.add_point(other)
		else:
			return self.add_tuple(other)

	def add_point(self,other):
		return Point(self.x + other.x,self.y + other.y)

	def add_tuple(self,other):
		return Point(self.x + other[0],self.y + other[1])

	def __radd__(self,other):
		return self.__add__(other)

	def __str__(self):
		return '(%d,%d)' %(self.x,self.y)


p=Point(3,4)
q=Point(6,2)
r=(1,7)

print p+q
print p+r
print r+q
