# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(lst)->list:
    new_lst = lst[1:-1]
    return new_lst

print(chop([1,2,3,5,6,7,8]))


def middle(lst)->list:
    new_list = lst[:]
    del new_list[1:-1]
    return new_list

print(middle([1,2,4,5,6]))