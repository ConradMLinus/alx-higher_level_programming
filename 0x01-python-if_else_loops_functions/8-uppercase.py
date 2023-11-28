#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')+1):
            cap = ord(i) - 32
        else:
            cap = ord(i)
        print("{}".format(chr(cap)), end="")
    print()
