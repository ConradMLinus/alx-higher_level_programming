#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if str.index(i) != n:
            print("{}".format(i), end="")
    return("")
