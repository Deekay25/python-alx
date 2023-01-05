print(list(range(10, 0, 2)))
print("new",list(range(0, -10, -2)))
print("{:d} Mission street, {}".format(972, "San Francisco"))

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
a = [1,2]
b = a + [3]
print(b)

a = (1, 2)
b = (1, 2)
print(a is b)