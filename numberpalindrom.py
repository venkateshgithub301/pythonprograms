n=1213121
temp=n
remainder=reverse=0
while(temp>0):
   remainder=temp%10
   temp=temp/10
   reverse=reverse*10+remainder
if((n)==reverse):
     print "num is palindrom"
else:
     print "num is not palindrom"
