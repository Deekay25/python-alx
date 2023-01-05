# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

#my solution
# name = 'banana'

# for i in range(len(name)-1,-1, -1):
#     print(name[i])

name = 'banana'
for i in range(len(name)):
    print(name[::-1][i])