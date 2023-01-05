"""
write a program that takes numbers as input
from the user then calculate the average of the numbers 
using sum(),len() functions. Numbers are to be stored 
in a list. if a user enters 'done', program terminates
"""

num = list()

while True:
    inp = input('Enter the number: ')
    if inp == 'done':
        break
    f_inp = float(inp)
    num.append(f_inp)
print(sum(num)/len(num))