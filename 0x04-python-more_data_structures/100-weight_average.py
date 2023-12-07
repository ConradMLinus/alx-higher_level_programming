#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    else:
        return (
            sum(list(i * j for i, j in my_list))
            / sum(list(j for i, j in my_list))
            )
