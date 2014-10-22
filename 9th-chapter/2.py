def has_no_e(wlist):
	notE=0
	total=0
	for word in wlist:
		if 'e' not in word:
			print word
			notE+=1
		total+=1

	print "\n\n\tpercentage of words not having 'e' is %d\n\n" %(notE*100/total)

has_no_e(['binoy','benoy','asde','dfgrt'])
