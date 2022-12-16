#i do not understand

#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(c), end='')
    print("")
print(uppercase("best"))




#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord('a') <= ord(s) <= ord('z'):
            s = chr(ord(s) - ord('a') + ord('A'))
        print("{:s}".format(s), end="")
    print()