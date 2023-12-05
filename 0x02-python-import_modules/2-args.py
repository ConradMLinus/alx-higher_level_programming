#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 1:
        print("{} argument:".format(count, ))
    elif count == 0:
        print("{} arguments.".format(count))
    else:
        print("{} arguments:".format(count))

    if count >= 1:
        count = 0
        for arg in argv:
            if count != 0:
                print("{}: {}".format(count, arg))
            count +=1
