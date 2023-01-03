# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
# create a function called computepay which takes two parameters
# (hours and rate).

hours = int(input('Hours: '))
rate = float(input('rate: ')) 
def computepay(hours : int, rate: float)-> float:
    if hours > 40:
        pay = (hours - 40) * rate * 1.5 + (40 * rate)
    else:
        pay = hours * rate
    return pay
print('pay: ',computepay(hours,rate))