class phone_book():
	def __init__ (self,d):

    	self.d = {}

   	def add_contact(self,name=None,number=None):
    	self.d[name]=number
        return self.d

    def get_contact(self,name=None):
        if name:
        	return self.d.get(name,"NOT FOUND")
p=phone_book()
a=p.add_contact('venkatesh','8985324655')
p.get_contact()
print p.get_contact('venkatesh')




