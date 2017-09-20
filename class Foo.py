class Foo(object):
     def __init__(self, frob, frotz):
          self.frobricate = frob
          self.frotz = frotz

class Bar(Foo):
     def __init__(self, frob, frizzle):
          super(Bar, self).__init__(frob, frizzle)
          self.frotz = 34
          self.frazzle = frizzle


bar = Bar(1,2)
print "frobricate:", bar.frobricate
print "frotz:", bar.frotz
print "frazzle:", bar.frazzle