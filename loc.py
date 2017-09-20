class cal():
  def __ini__(self,a,b):
  	self.a=a
  	self.b=b

  def add (self,a=8,b=5):
      if a and b:
             return a+b
      else:
             return self.a+self.b
  def sub (self,a=8,b=5):
  	  if a and b:
             return a-b
      else:
             return self.a-self.b
  def div (self,a=8,b=5)
      if a and b:
             return a/b
      else:
             return self.a/self.b:
  	
  def mul (self,a=8,b=5):
  	  if a and b:
             return a*b
      else:
             return self.a*self.b
f=cal()
print f.add(2,3)
print f.sub(2,3)
print f.div(2,3)
print f.mul(2,3)

