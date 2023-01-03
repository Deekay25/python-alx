#Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    hrs = float(input('Enter the number of hours worked: '))
    rate = float(input('Enter the rate: '))
except:
    print('Error, please Enter numeric input')
    quit()

if hrs > 40:
    pay =  (40 * rate) + (hrs - 40) * rate * 1.5
else:
    pay = hrs * rate
print('second ex pay:', float(pay))