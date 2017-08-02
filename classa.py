import pudb
class classA(object):
	def __init__(self):
		pudb .set_trace()
		print ("came to constructor")

	def func1(self):
		print ("firstclass func1")

if __name__ == '__main__':
	f = classA()
	f.func1()
	print ("hello")