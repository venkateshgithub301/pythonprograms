class parent():
   def add_fun(self,a,b):
       return a+b
class child1(parent):
	def sub_fun(self,a,b):
		return a-b
class child2(child1):
	def derived(self):
		print "multi level inheritance"

c=child2()
print c.sub_fun(12,2)
print c.add_fun(2,3)
c.derived()
