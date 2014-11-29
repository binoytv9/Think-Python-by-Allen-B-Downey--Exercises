"""	Image viewer	"""

def getfilenames(directory):
	for filename in os.listdir(directory):
		if os.path.isfile(filename):
			yield filename

file_list = getfilenames('.')
def next_file():
	for
import os
from Gui import *
from Tkinter import *

from PIL import Image as PIL
import ImageTk



g=Gui()
g.title('Image viewer')

c=g.ca(width=500,height=500)

image_viewer('.')
g.bu(image=p2)



"""
			try:
				image = PIL.open(filename)
				photo = ImageTk.PhotoImage(image)
				c.image([0,0],image=photo)
			except IOError:
				continue
p=PhotoImage(file='danger.gif')
c.image([0,0],image=p)

image=PIL.open('allen.png')
p2=ImageTk.PhotoImage(image)


"""


g.mainloop()
