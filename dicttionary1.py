dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;               # update existing entry
dict['School'] = "DPS School";
if (key=Name):
       print "value is found"
else:
       print "value not found" # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
print dict                     #after updating the dictionary
print dict.items()

dict = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  dict.setdefault('Age', None)#default values are return when the given value
                                                  #is not occre in the  dictionary to define by default keyword

print "Value : %s" %  dict.setdefault('Sex', None)

