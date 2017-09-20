class cal():
    def __init__(self,c,y):
       self.a=c
       self.b=y
    def add(self,a=None,b=None):
        if a and b:
           return a+b
        elif a and not b:
            return a+self.b
        elif not a and b:
            return self.a+b
        else:
             return self.a+self.b
c=cal(22,21)
print c.add(20,19)
print c.a, c.b



