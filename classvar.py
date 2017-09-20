#import pudb
class classvar():
	def __init__(self,x,y):
		"""
		constructor of class, accepts the two argument while calling class instance
		and asigns the arguments to class variable var1 and var2
		"""
		# pudb.set_trace()
		self.var1 = x
		self.var2 = y
	def class_arg_fun(self):
		return self.var1 + self.var2

if __name__ == '__main__':
 c = classvar(10,20)
#pudb.set_trace()
print c.class_arg_fun()