"""	Write a program that creates a Canvas and a Button. When the user presses the Button,
	it should draw a circle on the canvas	"""

def draw_circle():
	item=c.circle([0,0],100,fill='red')

from Gui import *

g=Gui()

b1 = g.bu(text='Create a Circle',command=draw_circle)
c = g.ca(width=500,height=500)


g.mainloop()
