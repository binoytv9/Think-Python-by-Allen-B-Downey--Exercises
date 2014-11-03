"""	Write a function named move_rectangle that takes a Rectangle and two numbers
	named dx and dy . It should change the location of the rectangle by adding dx to the x
	coordinate of corner and adding dy to the y coordinate of corner	"""


class rectangle(object):
	""" contains length breadth and a lower left corner point """

class point(object):
	""" a point in 2D space """

def move_rectangle(rect,dx,dy):
	rect.corner.x+=dx
	rect.corner.y+=dy

def print_rect(rect):
	print rect.height
	print rect.breadth
	print (rect.corner.x,rect.corner.y)
	print '\n\n'


box=rectangle()
box.height=50
box.breadth=20
box.corner=point()
box.corner.x=3
box.corner.y=8

print_rect(box)
move_rectangle(box,2,3)
print_rect(box)
