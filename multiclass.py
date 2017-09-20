#import pudb
class classA(object):
	def __init__(self):
		print ("class A constructor")

	def add_fun(self,a,b):
		print ("class A add_fun")
		return a+b


class classB(object):
	def __init__(self):
		print ("class B constructor")

	def add_fun(self,a,b):
		print ("class B add_fun")
		return a+b

class child(classA, classB):
	def __init__(self,a,b):
		super(child, self).__init__()
		print ("child constructor")

	def add_fun(self,a,b):
		print ("child class add_fun")
		#pudb.set_trace()
		return super(child, self).add_fun(a,b)
		return a+b

if __name__ == '__main__':
	c = child(7,9)
	print c.add_fun(10,20)