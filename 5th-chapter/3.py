def check_fermat(a,b,c,n):
	if (n>2) and (a**n + b**n == c**n):
		print "\n\t\tHoly smokes, Fermat was wrong!"
	else:
		print "\n\t\tNo, that doesn't work."

a = raw_input("enter value for a : ")
b = raw_input("enter value for b : ")
c = raw_input("enter value for c : ")
n = raw_input("enter value for n : ")

check_fermat(int(a),int(b),int(c),int(n))
