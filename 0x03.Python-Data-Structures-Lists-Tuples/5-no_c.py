#!/usr/bin/python3

# def no_c(my_string):
#     result = ''
#     for chr in my_string:
#         if 'c' in chr or 'C' in chr:
#             continue
#         else:
#             result = result + chr
#     return result

#another way
# def no_c(my_string):
#     result = ''
#     for chr in my_string:
#         if chr == 'c' or chr == 'C':
#             continue
#         else:
#             result = result + chr
#     return result

#using lsit comprehension
# def no_c(my_string):
#     str = [c for c in my_string if (c != 'C' and c != 'c')]
#     return ''.join(str)

# a one liner
def no_c(my_string):
    # return ''.join(c for c in my_string if c != 'c' and c != 'C')
    return ''.join(c for c in my_string if c not in 'cC')