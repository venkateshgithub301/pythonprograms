#import pudb
class calculation():
	def __init__(self,x,y):
		"""
		constructor of class, accepts the two argument while calling class instance
		and asigns the arguments to class variable var1 and var2
		"""
		self.var1 = x
		self.var2 = y
	def add_fun(self, a=None, b=None):
		#pudb.set_trace()
		if a and b:							# if a and b both are passed
			return a+b
		elif not a and not b:				# if a and b both not passed
			return self.var1 + self.var2
		elif a and not b:					# if a is passed, but not b
			return a + self.var2
		else:
			return self.var1 + b 			# if a is not passed, but b is passed

	def mul_fun(self, a,b):
		return a*b

	def sub_fun(self, a,b):
		return b-a


if __name__ == '__main__':
	c = calculation(10,20)
	print c.add_fun()
	print c.add_fun(2,3)
	print c.add_fun(a=2)
	print c.add_fun(b=3)

	print c.mul_fun(2,3)
	print c.sub_fun(3,7)