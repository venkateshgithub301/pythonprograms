class cal():
    def __init__(self, x,y):
	self.x=x
	self.y=y
    def add(self,x=None,y=None):
    	if x and not y:
    	   return x+self.y
c=cal(10,20)
print c.add(x=5)
