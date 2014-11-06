"""	Write a program that creates a GUI with a single button. When the button is pressed it should create a second button.
	 When that button is pressed, it should create a label that says, "Nice job!"	"""

def create_button():
	b2=g.bu(text='Press me again!!',command=create_label)

def create_label():
	l1=g.la(text='Nice job!')

from Gui import *

g=Gui()
b1=g.bu(text='Press me!',command=create_button)


g.mainloop()
