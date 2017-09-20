class venki(object):
    #def__init__(self):
    #print("this is parent clas")
    def add_fun(self,a,b):
        return a+b   
class naresh(venki):
	#def__init__(self):
		#print ("this is child class")
	def sub_fun(self,a,b):
		return a-b
class hrithic(naresh):
	def init(self,a,b):
	    print("this is derived from the derived class")
	    return super(hrithic,self).sub_fun(a,b)
	    
	    
c=hrithic()
c.sub_fun(11,10)
c.add_fun(12,1)
c.init(12,2)

