class parent():
   def add(self,a=10,b=20):
       return a+b
class child(parent):
    pass
c=child()
print c.add()