def grid():
	box()
	box()
	hor()

def box():
	hor()
	ver()

def hor():
	print '+ - - - - + - - - - +'

def ver():
	for i in range(4):
		print '|         |         |'


grid()
