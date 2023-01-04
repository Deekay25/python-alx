# very important program

# Exercise 3: Encapsulate this code in a function named count, 
# and generalize it so that it accepts the string and the letter as arguments.
# example:
# countLetters("banana", "a")
# 3
# countLetters("banana", "b")
# 1
# countLetters("banana", "n")
# 2
# >>>

def count(str, letter):
    count = 0
    for char in str:
        if char == letter:
            count = count + 1
    return count
print(count('banana', 'a'))


name = 'aisha'
index = len(name) -1
while index >= 0:
    print(name[index], end= ' ')
    index = index - 1


