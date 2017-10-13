
add=lambda x,y:dict(zip(x,y))
print add([1,2,3,9],[9,8,7,6])
print reduce(lambda a,b:a+b,range(1,100))
print filter(lambda a:a%2==0,range(1,10))
print [ele if ele%2==0 else None for ele in range(1 ,50)]#list comprehension
print [ele for ele in range(1,100) if ele%3==0 and ele%5==0]
