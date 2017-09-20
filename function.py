def parent(num):
    def first_child():
        return "printing from the first_child()fuction"
    def second_child():
        return "printing from the second_child()function"


    try :
        assert num == 0
        return first_child
    except AssertionError:
        return second_child


foo= parent(10)
bar= parent(11)

print (foo)
print (bar)

print (foo())
print (bar())

