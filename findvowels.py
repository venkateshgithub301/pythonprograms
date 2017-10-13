#Python script to find vowels in a string
#print "Enter a string:"
 
#define i
i = 0;
 
#get the input string
inpstr = 'heloo world'#raw_input()
 
#convert string to lower case
inplower = inpstr.lower()
 
vowels = ['a','e','i','o','u']
 
#loop through each character 
for c in inplower:
    #if vowel found then increment i
    if c in vowels:
        i = i + 1
 
#print output
print "Number of vowels: "+ str(i)