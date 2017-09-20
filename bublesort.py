#import pudb
list = [5,2,10,1,8,6,4,9]

def bubble(list):
    length = len(list) - 1
    sorted = False
    #pudb.set-trace()
    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]

bubble(list)
print list
 
