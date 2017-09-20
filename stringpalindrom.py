my_str='aiBoBiA'
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
   print "given str is palindrom"
else:
   print "given str is not palindrom"


# change this value for a different output
#my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
#my_str = my_str.casefold()

# reverse the string
#rev_str = reversed(my_str)

# check if the string is equal to its reverse
#if list(my_str) == list(rev_str):
 #  print("It is palindrome")
#else:
 #  print("It is not palindrome")