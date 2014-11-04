"""	Write a str method for the Point class. Create a Point object and print it.	"""


class Point(object):
	""" representation of a point in 2D space """
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __str__(self):
		return '(%d,%d)'%(self.x,self.y)


p=Point()
print p
q=Point(2)
print q
