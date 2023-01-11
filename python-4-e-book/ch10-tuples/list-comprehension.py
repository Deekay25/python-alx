# For
# example, if you wanted to convert a list of strings – each string storing digits – into
# numbers that you can sum up, you would write:

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = []
# for x in list_of_ints_in_strings:
#     list_of_ints.append(int(x))
# print(sum(list_of_ints))

# with list comprehension
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [int(x) for x in list_of_ints_in_strings]
print(sum(list_of_ints))