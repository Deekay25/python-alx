# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

min = None
max = None
while True:
    num = input('Enter number: ')
    if num == 'done':
        break
    try:
        num_f = float(num)
    except:
        print('invalide data')
        continue
    if max is None or num_f > max:
        max = num_f
    if min is None or num_f < min:
        min = num_f
print('max: ', max, 'min: ', min)
