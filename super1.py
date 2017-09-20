class parent():
    def add(self,a=10,b=20):
        return a+b
class child(parent):
    def add(self,a=10,b=2):
     	return a+b
c=child()
print (c.add())
