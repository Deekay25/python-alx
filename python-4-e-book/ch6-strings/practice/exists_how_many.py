# write a simple loop that loops through each letter in a
# strng and count the number of times the loop encounters 'a'
# character
# --> Count How many times a exits below
# --> use both while loop and for loop

# fruit = 'banana'
# count = 0
# for i in fruit:
#     if i == 'a':
#         count = count + 1
# print(count)

#while loop

fruit = 'banana'
count = 0
index = 0
while index < len(fruit):
    if fruit[index] == 'a':
        count = count + 1
        print(fruit[index], count)
    index = index + 1
print(count)