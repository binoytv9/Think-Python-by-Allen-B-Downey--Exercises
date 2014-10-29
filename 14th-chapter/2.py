def sed(pstr,rstr,fn1,fn2):
	try:
		f1=open(fn1)
		f2=open(fn2,'w')

		for line in f1:
			f2.write(line.replace(pstr,rstr))
		f1.close()
		f2.close()
	except:
		print "\n\terror\n"

sed('file','FILE','a.txt','b.txt')
