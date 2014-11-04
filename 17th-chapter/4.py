"""	Write an add method for the Point class	"""


class Point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __add__(self,other):
		return Point(self.x + other.x,self.y + other.y)

	def __str__(self):
		return '(%d,%d)' %(self.x,self.y)


p=Point(1,2)
q=Point(5,6)

print p+q

