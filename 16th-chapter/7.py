import datetime

def current_date():
	today=datetime.date.today()
	print 'today is ',today
	print 'day of the week is ',today.ctime().split()[0]
