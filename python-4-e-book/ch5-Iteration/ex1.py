# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333


# get an input from user
# repeatedly listen to the input using while loop
# use contunue to the iteration
# use break to kill operation
# return total, count and average of the numbers



count = 0
sum = 0
while True:
    user = input("Enter a number: ")
    if user == 'done':
        break
    try:
        user_num = int(user)
    except: 
        print("Invalid input")
        continue
    count = count + 1
    sum = sum + user_num
print('total: ', sum, 'count: ', count, 'average: ', sum/count)