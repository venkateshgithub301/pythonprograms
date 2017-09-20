num=[1,1,1,2,2,2,3,4,3,3,5,6,7,8,9,10]
my_set={n for n in num}
print my_set
            (or)// my_set=set()
for n in num:
	my_set.add(n)
	print my_set//