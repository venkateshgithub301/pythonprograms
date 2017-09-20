class parent(object):
     def foveriding(self,a,b):
          self.a=a
          self.b=b

class child(parent):
     def foveriding(self,a=12,b=10):
          super(child, self).foveriding(a,b)
          return a+b
      


bar = child()
bar.foveriding()
print bar