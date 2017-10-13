def even(l):
	yield(i for i in l if i%2==0)
	x=even(range(10))
print x.next()
