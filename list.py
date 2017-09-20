l=[1,2,3,4,5]
count=0
l1=[]
for i in range (6):
   if i%2==1:
    count+=i
    l1.append(count)
    print l1
else:
	print "number is even"
