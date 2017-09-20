class parent:
   def add(self,a=78,b=10):
       return a+b
class child(parent):
	n=2
    
c=child()
print c.add()