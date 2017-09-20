def add(a,b):
  c=a+b
  return c
c=add(1,9)
print c
def handle_error(add):
   def wrapper(*args,**kwargs):
      try:
          return add(*args,**kwargs)
      except exception as e:
          return e
      return wrapper
