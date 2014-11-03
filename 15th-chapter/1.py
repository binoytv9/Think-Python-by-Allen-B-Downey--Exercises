"""	Write a function called distance_between_points that takes two 
	Points as arguments and returns the distance between them.	"""


class Point(object):
	""" represent a point in 2D space """

def distance_between_points(p1,p2):
	return math.sqrt( (p1.x-p2.x)**2 + (p1.y-p2.y)**2 )


import math

p1=Point()
p2=Point()

p1.x=9
p1.y=7

p2.x=3
p2.y=2

print distance_between_points(p1,p2)
