def time_in(fun):
	def wrapper(*args,**kwargs):
		result=fun(*args,**kwargs)
		return result
	return wrapper


@time_in
def produvt(a):
	c=[]
	for i in a:
	 c.append(i*i)
 	return c

p=[2,3,4,5]
d=produvt(p)
print d