"""	Modify your solution to Exercise 19-2 by adding an Entry widget and a second button.
	When the user presses the second button, it should read a color name from the Entry
	and use it to change the fill color of the circle	"""



def create_circle():
	global item
	item = c.circle([0,0],100,fill='red')

def change_color():
	try:
		if 'item' in globals():
			item.config(fill=entry.get())
		else:
			g.la(text='First create a circle!!!')
			return
	except :
		g.la(text='Invalid color')
		

from Gui import *

g = Gui()
b1 = g.bu(text='Press to create a circle',command=create_circle)
c = g.ca(width=500,height=500)

entry=g.en(text='enter the color')
b2 = g.bu(text='Press to change color of circle',command=change_color)



g.mainloop()
