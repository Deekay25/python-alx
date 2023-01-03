# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

hrs = float(input('Enter the number of hours worked: '))
rate = float(input('Enter the rate: '))

if hrs > 40:
    pay =  (40 * rate) + (hrs - 40) * rate * 1.5
else:
    pay = hrs * rate
print('pay:', float(pay))