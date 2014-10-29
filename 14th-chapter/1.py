def walk(dname):
	for root,subdir,filenames in os.walk(dname):
		for filename in filenames:
			print os.path.join(root,filename)

import os
walk('..')
