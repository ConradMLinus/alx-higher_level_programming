#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = []
    for i in argv[1:]:
        args.append(int(i))
    print(sum(args))
