for n in range(10,20):
   for i in range(2,n):
   	if (n%i)==0:
         print n,"is not prime number"
         break
   else:
     	 print n,"is a prime number"