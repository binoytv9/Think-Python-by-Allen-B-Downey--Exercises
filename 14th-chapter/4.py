def search(suffix):
	l=[]
	for root,dirs,files in os.walk('..'):
		for fname in files:
			if fname[-len(suffix):] == suffix:
				l.append(os.path.join(root,fname))
	return l


def md5_dict(lst):
	d={}
	for fpath in lst:
		d.setdefault(os.popen('md5sum '+ fpath).read()[:32],[]).append(fpath)
	return d


def duplicate():
	d=md5_dict(search('.txt'))
	for v in d.values():
		if len(v) > 1:
			print v


import os
duplicate()
