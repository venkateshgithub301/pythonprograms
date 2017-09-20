n = input("\nEnter any number to check for palindrome:")
temp = n
remainder = reverse = 0
while (temp > 0) :
    remainder = temp % 10
    temp = temp / 10
    reverse = reverse *10 + remainder
if(int(n) == reverse) :
    print "\n\t\tGiven number " +str(n)+" is palindrome"
else :
    print "\n\t\tGiven number " +str(n)+" is not a palindrome"
