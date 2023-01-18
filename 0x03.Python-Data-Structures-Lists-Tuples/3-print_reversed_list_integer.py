#!usr/bin/python3

# def print_reversed_list_integer(my_list=[]):
#     if my_list:
#         for ls in my_list[::-1]:
#             print('{}'.format(ls))

#using list comprehension
def print_reversed_list_integer(my_list=[]):
    if my_list:
        [print('{}'.format(ls)) for ls in my_list[::-1]]

