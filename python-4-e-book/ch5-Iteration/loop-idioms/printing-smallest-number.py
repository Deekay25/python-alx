# the program is wrong  because smallest so far will always be -1
# smaller_so_far = -1

# for num in [1,10,22,45,73,27]:
#     if num < smaller_so_far:
#         smaller_so_far = num
#     print(smaller_so_far, num) 


smallest_so_far = None

for num in [1,10,22,45,73,27]:
    # using just 'if num < smallest_so_far: ' is wrong
    # because you cannot compare none types <,> etc
    if smallest_so_far is None or num < smallest_so_far:
        smallest_so_far = num
    print(num, smallest_so_far)
print(smallest_so_far)