#!/usr/bin/python3
from ast import operator


if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a, opp, b = int(argv[1]), argv[2], int(argv[3])
        if opp == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        elif opp == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        elif opp == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        elif opp == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
