def histogram(lst):
	d={}
	for element in lst:
		d[element]=d.get(element,0) + 1
	return d


def choose_from_hist(h):
	sum=0.0
	for key in h:
		sum+=h[key]
	new={}
	for key in h:
		new[key]=h[key]/sum

	return new

t = ['a', 'a', 'b']
hist = histogram(t)
print hist
hist = choose_from_hist(hist)
print hist
