# # numbers to be printed from 1 to 100 seprated by a space
def fizzbuzz():
    for i in range(1, 101):
        # multiples of 3 print fizz
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz", end= ' ')
        elif i % 3 == 0:
            print("fizz", end=' ')
        elif i % 5 == 0:
            print("buzz", end=' ')
        else:
            print(i, end= ' ')
# multiple of 5 print buzz
# multiples of botth print fizzbuzz

print(fizzbuzz())

#!/usr/bin/python3
#alx accepted
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end='')
        if i % 5 == 0:
            print("Buzz", end='')
        if i % 3 and i % 5:
            print("{:d}".format(i), end='')
        print(end=' ')
print(fizzbuzz())


