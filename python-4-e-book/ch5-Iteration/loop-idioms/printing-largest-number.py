# largest_so_far = -1

# print('before: ', largest_so_far)
# for num in [1,10,8,7,11,5]:
#     if num > largest_so_far:
#         largest_so_far = num
#         # print(num,largest_so_far)
#     print(num, largest_so_far)
# print('num',largest_so_far)

#using the none type
#the most efficient way to do it
# it represents emptyness
# use the 'is' and 'is not' keyword with None types and booleans

# largest_so_far = None
# for num in [3,5,15,2,32,19,10]:
#     if largest_so_far is None:
#         largest_so_far = num
#     elif num > largest_so_far:
#         largest_so_far = num 
#     print(largest_so_far, num)
# print('large: ', largest_so_far)


# refactoring the above the code
largest_so_far = None

for num in [3,5,15,2,32,19,10]:
    if largest_so_far is None or num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print('last-large: ', largest_so_far)