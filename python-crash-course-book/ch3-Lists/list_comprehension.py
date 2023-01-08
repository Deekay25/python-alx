# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

"""
output --> 1 ^ 3 = 1
       --> 2 ^ 3 = 8
       .
       .
       .
       --> 10 ^ 3 = 1000
"""

#make a list of first 10 cubes from 1 to 10
cubes = [1,2,3,4,5,6,7,8,9,10]

#use a for loop to pirnt each cube
for cube in cubes:
    print(cube, '=',cube**3)
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

lst = [cube**3 for cube in cubes]
print('from list comprehension', lst)