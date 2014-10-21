def is_triangle(a,b,c):
	if (a>b+c) or (b>a+c) or (c>a+b):
		print "No"
	else:
		print "Yes"

a=raw_input("enter 1st stick length : ");
b=raw_input("enter 2nd stick length : ");
c=raw_input("enter 3rd stick length : ");

is_triangle(int(a),int(b),int(c))
