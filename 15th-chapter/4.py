class canvas(object):
	""" canvas """

class rectangle(object):
	""" rectangle """

class point(object):
	""" point """

class circle(object):
	""" circle """

def draw_rectangle(c,r):
	world=World()
	can=world.ca(width=c.w,height=c.h,background='white')
	bbox=[[r.p1.x,r.p1.y],[r.p2.x,r.p2.y]]
	can.rectangle(bbox,outline='black',width=0,fill=r.color)
	world.mainloop()


def draw_circle(c,cir):
	world=World()
	can=world.ca(width=c.w,height=c.h,background='white')
	can.circle(cir.o,cir.r,outline='black',width=2,fill='red')
	world.mainloop()


def draw_point(c,p):
	world=World()
	can=world.ca(width=c.w,height=c.h,background='white')
	pt=[[p.x,p.y],[p.x,p.y]]
	can.rectangle(pt)
	world.mainloop()

def czech_flag():
	c=canvas()
	c.w=500
	c.h=500

	r1=rectangle()
	r1.color='red'

	r1.p1=point()
	r1.p1.x=-200
	r1.p1.y=-200

	r1.p2=point()
	r1.p2.x=200
	r1.p2.y=0

	r2=rectangle()
	r2.color='white'
	r2.p1=point()
	r2.p1.x=-200
	r2.p1.y=0

	r2.p2=point()
	r2.p2.x=200
	r2.p2.y=200

	world=World()
	can=world.ca(width=c.w,height=c.h,background='white')

	bbox1=[[r1.p1.x,r1.p1.y],[r1.p2.x,r1.p2.y]]
	can.rectangle(bbox1,outline='black',width=1,fill=r1.color)

	bbox2=[[r2.p1.x,r2.p1.y],[r2.p2.x,r2.p2.y]]
	can.rectangle(bbox2,outline='black',width=1,fill=r2.color)

	points = [[-200,-200], [-200, 200], [0, 0]]
	can.polygon(points, fill='blue')

	world.mainloop()


from swampy.World import World

c=canvas()
c.w=500
c.h=600

r=rectangle()
r.color='green4'
r.p1=point()
r.p1.x=150
r.p1.y=200

r.p2=point()
r.p2.x=-130
r.p2.y=-190

p=point()
p.x=100
p.y=200

cir=circle()
cir.o=[4,5]
cir.r=80

#draw_rectangle(c,r)
#draw_point(c,p)
#draw_circle(c,cir)
czech_flag()
