#my solution (which happens to be wrong)
# def print_last_digit(number):
#     if number < 0:
#         remainder = number % -10
#     else:
#         remainder = number % 10
    
#     return remainder

# print(print_last_digit(-98))

#my alx accepted solution
#the program returns the last digit
#and the value of the last digit
def print_last_digit(number):
    if number < 0:
        remainder = number % -10
        print("{:d}".format(-remainder), end='')
        return -remainder
    else:
        remainder = number % 10
        print("{:d}".format(remainder), end='')
        return remainder
print(print_last_digit(235))

#github inspired
#!/usr/bin/python3
# def print_last_digit(number):
#     if number < 0:
#         last = number % -10
#         print("{:d}".format(-last), end="")
#         return -last
#     print("{:d}".format(number % 10), end="")
#     return number % 10
# print(print_last_digit(1))


#git hub inspired
#!/usr/bin/python3
# def print_last_digit(number):
#     if number < 0:
#         print("{:d}".format(-(number % -10)), end='')
#         return(-(number % -10))
#     else:
#         print("{:d}".format(number % 10), end='')
#         return(number % 10)
# print(print_last_digit(-234))