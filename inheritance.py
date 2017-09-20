#import pudb
class parent(object):
	def __init__(self,x,y):
		self.var1=x
		self.var2=y
		print ("parent constructor")

	def add_fun(self,a,b):
		print ("Came to parent add_function")
		return self.var1 + self.var2 #a+b

class child(parent):
	def __init__(self, x, y):
		super(child, self).__init__(x, y)
		print ("child constructor")

	def add_fun(self,a,b,c):
		print ("Came to child add_function")
		r=super(child, self).add_fun(a,b)
		return r+c

if __name__ == '__main__':
	c = child(10,20)
#pudb.set_trace()
print c.add_fun(10,20,30)