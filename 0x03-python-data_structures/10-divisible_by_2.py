#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checker = my_list.copy()
    for i in my_list:
        if i % 2 != 0:
            checker[my_list.index(i)] = False
        else:
            checker[my_list.index(i)] = True
    return (checker)
