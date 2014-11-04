class Kangaroo(object):
	def __init__(self,pouch_contents=[]):
		self.pouch_contents = pouch_contents

	def put_in_pouch(self,item):
		self.pouch_contents.append(item)

	def __str__(self):
		t = [ object.__str__(self) + ' with pouch contents:' ]
		for obj in self.pouch_contents:
			s = '    ' + object.__str__(obj)
			t.append(s)
		return '\n'.join(t)

kanga=Kangaroo()
roo=Kangaroo()

kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print kanga
print roo
