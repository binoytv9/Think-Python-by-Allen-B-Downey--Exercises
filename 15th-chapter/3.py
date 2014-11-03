"""	Write a version of move_rectangle that creates and 
	returns a new Rectangle instead of modifying the old one	"""


class rectangle(object):
	""" contains length breadth and a lower left corner point """

class point(object):
	""" a point in 2D space """

def move_rectangle(rect,dx,dy):
	new_rect=copy.deepcopy(rect)
	new_rect.corner.x+=dx
	new_rect.corner.y+=dy
	return new_rect

def print_rect(rect):
	print rect.height
	print rect.breadth
	print (rect.corner.x,rect.corner.y)
	print '\n\n'

import copy

box=rectangle()
box.height=50
box.breadth=20
box.corner=point()
box.corner.x=3
box.corner.y=8

new_box=move_rectangle(box,2,3)

print 'old box\n'
print_rect(box)

print 'new box\n'
print_rect(new_box)
