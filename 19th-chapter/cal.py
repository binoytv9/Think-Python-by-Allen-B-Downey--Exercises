def insert(obj):
	cal_in.insert(END,obj)

def delete(p):
	cal_in.delete(p)
	print p,len(cal_in.get())-1,cal_in.get()

from Gui import *

cal=Gui()
cal.title('Calculator')

cal_in = cal.en(width=35)

cal.row()
cal.gr(cols=6)

seven = cal.bu(text='7',command = Callable(insert,'7'))
eight = cal.bu(text='8',command = Callable(insert,'8'))
nine = cal.bu(text='9',command = Callable(insert,'9'))
div = cal.bu(text='/',command = Callable(insert,'/'))

#bspace = cal.bu(text='Del',command = Callable(delete,0))
bspace = cal.bu(text='Del',command = Callable(delete,len(cal_in.get())-1))

clr = cal.bu(text='Clr',command = Callable(delete,'7'))

four = cal.bu(text='4',command = Callable(insert,'4'))
five = cal.bu(text='5',command = Callable(insert,'5'))
six = cal.bu(text='6',command = Callable(insert,'6'))
mul = cal.bu(text='*',command = Callable(insert,'*'))
lbra = cal.bu(text='(',command = Callable(insert,'('))
rbra = cal.bu(text=')',command = Callable(insert,')'))

one = cal.bu(text='1',command = Callable(insert,'1'))
two = cal.bu(text='2',command = Callable(insert,'2'))
three = cal.bu(text='3',command = Callable(insert,'3'))
minus = cal.bu(text='-',command = Callable(insert,'-'))
sqr = cal.bu(text='sqr(x)',command = Callable(insert,'7'))
sroot = cal.bu(text='sqrt(x)',command = Callable(insert,'7'))

zero = cal.bu(text='0',command = Callable(insert,'0'))
dot = cal.bu(text='.',command = Callable(insert,'.'))
per = cal.bu(text='%',command = Callable(insert,'%'))
plus = cal.bu(text='+',command = Callable(insert,'+'))
equal = cal.bu(text='=',command = Callable(insert,'='))


cal.mainloop()
