class parent():
   
  
    def add(self,a,b):
    	return a+b
class child(parent):
	def sub(self,a,b):
    	  return a-b
d=parent()      
c=child()

e=d.add(8,12)
f=c.sub(12,8)
print e
print f

