#print 10 most common words from romeo-full.txt
# solve with list comprehension as well
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

#this means give me from 0 to 10 from the list that you have already sorted
for key, val in lst[:10]:
    print(key, val)