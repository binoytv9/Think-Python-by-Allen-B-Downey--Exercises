def antihtml(url):
	page=urllib.urlopen(url).read()
	antitag=re.sub(r'\s*<.*?>\s*','\n',page,flags=re.S)
	return antitag.split()


def zip_code():
	zipc=raw_input("\n\nenter the zip code : ")
	bname='http://www.uszip.com/zip'
	con = antihtml(os.path.join(bname,zipc.strip(string.punctuation+string.whitespace)))
	if con[0] == ',':
		print "\n\n%s zip code not found!!!\n\n" %zipc
		return
	else:
		print "\n\n\tName of town : %s" %(con[0]+con[1])
		i=con.index('population')
		print "\tTotal population is %s\n\n" %con[i+1]



import re
import os
import urllib
import string

zip_code()
