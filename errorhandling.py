
def add_fun(a,b):
    c=a+b
    return c
c=add_fun(10,20)
print c
def handle_error(fun):
   def wrapper(*args,**kwargs):
      try:
          return fun(*args,**kwargs)
      except exception as e:
              return e
      return wrapper

