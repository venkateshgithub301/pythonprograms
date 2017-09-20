import pudb
a=5
def rec (n):
	if n<=1:
		return 1
	pudb.set_trace()
	return n * rec(n-1)
	

	

print rec(a)