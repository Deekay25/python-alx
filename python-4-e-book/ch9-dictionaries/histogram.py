# Write a program that loops through a string then count how many times each character exists in the 
# string, then update the result into a dictionary. 
# Do the same program with .get() method

# practtice
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# print(counts.get('jan', 0))
# 100
# print(counts.get('tim', 0))
# 0
# print(counts)

# word = 'brontosaurus'
# dic = dict()
# for char in word:
#     if char not in dic:
#         dic[char] = 1
#     else:
#         dic[char] = dic[char] + 1
# print(dic)

word = 'brontosaurus'
dic_2 = dict()
for char in word:
    dic_2[char] = dic_2.get(char,0) + 1
print(dic_2, 'dic2')
# The use of the get method to simplify this counting loop ends up being a very
# commonly used “idiom” in Python and we will use it many times in the rest of the
# book. So you should take a moment and compare the loop using the if statement
# and in operator with the loop using the get method. They do exactly the same
# thing, but one is more succinct

# other .get use cases
# .get('keyfromdic') // returns none if the key does not exist
# .get('keyfromdic', 'key you are looking for does not exist') // retuns the what was the written on the second arg if key does not exist