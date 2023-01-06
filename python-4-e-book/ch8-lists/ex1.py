# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
"""
output --> [1,2,3,4] --> [2,3] function returns None
output --> [1,2,3,4] --> [1,2,3,4] function returns [2,3]

some important things to know
t[1:-1] returns elements without first and last elements
del[1:-1] returns only the first and the last element
"""
#very important exercise
def chop(n):
    # n[1:-1] 
    del n[0]
    del n[-1]
    # n.pop(0) //works correct too
    # n.pop(-1)
chop_list = [1,2,3,4]
print(chop(chop_list)) # for both cases of del n[0] del n[-1] and n[1:-1] the function prints None
print(chop_list) #for del n[0] it prints [2,3] but if i use n[1:-1] it prints [1,2,3,4]

def middle(n):
    t = n[:]
    return t[1:-1]

middle_list = [1,2,3,4]
print(middle(middle_list)) # returns [2,3]
print(middle_list) # returns [1,2,3,4] unchanged
