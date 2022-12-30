#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    for i in range(len(sys.argv[1:])):
        print(add(sys.argv[i + 1],sys.argv[i]))