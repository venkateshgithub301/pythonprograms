#import pudb
class phone():
  def __init__(self):
     self.d={}
     
  def add_contact(self,name=None,number=None):
      self.d[name]=number
      return self.d
  def get_contact(self,name=None):
        if name:
            return self.d.get(name,"not found") 
#pudb.set_trace()   
p=phone()
a=p.add_contact('python','8985324655')
p.get_contact()
print p.get_contact('python')

