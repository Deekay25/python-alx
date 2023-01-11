# sort the dictionary by value d = {'a':10, 'b':1, 'c':22}

d = {'a':10, 'b':1, 'c':22}
l = list()
for key,value in d.items():
    l.append((value,key))
l.sort(reverse=True)
print(l)