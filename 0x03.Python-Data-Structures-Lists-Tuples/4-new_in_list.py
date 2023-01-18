#!/usr/bin/python3

# def new_in_list(my_list, idx, element):
#     my_list_copy = my_list[:]
#     if idx < 0 or idx > len(my_list_copy)-1:
#         return my_list
#     else:
#         my_list_copy[idx] = element
#     return my_list_copy
#another way
def new_in_list(my_list, idx, element):
    # I jst learn using list comprehension like below
    # saving it to a variable returns a copy of a list
    # unlike using normal for loop, it extract the values then return them
    new_list = [i for i in my_list] 
    if idx < 0 or idx > len(new_list)-1:
        return my_list
    else:
        new_list[idx] = element
    return new_list
new_in_list([1,2,3,4],2,8)