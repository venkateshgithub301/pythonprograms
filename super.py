class parent(object):
	def add(self,a=13,b=12):
		return a+b

class child(parent):
    def add(self,a=130,b=12):
         return super(child,self).add(a,b)

c=child()
print c.add()
