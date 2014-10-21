def hypotenuse(x,y):
	print 'x = ',x
	print 'y = ',y
	print
	xsquare = x**2
	ysquare = y**2
	print 'xsquare = ',xsquare
	print 'ysquare = ',ysquare
	print
	squaresum = xsquare+ysquare
	print 'squaresum = ',xsquare+ysquare
	print
	hypot=math.sqrt(squaresum)
	print 'hypotenuse is : ',hypot
	print

import math
hypotenuse(1,2)
