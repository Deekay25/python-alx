# dic = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

# for c in dic:
#     print(c, dic[c])

# If you want to print the keys in alphabetical order, you first make a list of the keys
# in the dictionary using the keys method available in dictionary objects, and then
# sort that list and loop through the sorted list, looking up each key and printing
# out key-value pairs in sorted order as follows:

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# convert the dictionary keys to a list using .keys()
dic = dict()
lst = list(counts.keys())
print(lst)
# sort the list
lst.sort()
print(lst)
# loop thrugh the sorted list
for key in lst:
    print(key, counts[key])

