class parent():

	def add(self,a,b):
		return a+b
class child(parent):
	def sub(self,a,b):
		return a-b
d=parent()      
c=child()

print d.add(9,7)
print c.sub(9,10)

