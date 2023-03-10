# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# The program produces the following output:
# Sat
# Fri
# Fri
# Fri

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From '):
#         line = line.split()
#         print(line[2])

# #better approach
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '): continue
#     line = line.split()
#     print(line[2])

#another way

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.split()
#     print('debug',line)
#     if line[0] != 'From ': continue //this fialed when it reaches an empty line
#     print(line[2])

# solution to above immediate program
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.split()
#     print('debug',line)
#     if len(line) == 0 : continue
#     if line[0] != 'From': continue
#     print(line[2])

# Exercise 2: Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

# for exercise 1, it cannot handle properly when a file liine contains only from 
# therefore, the below program fixes that 
# the below program is important to understand
fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])

# Exercise 3: Rewrite the guardian code in the above example without
# two if statements. Instead, use a compound logical expression using
# the or logical operator with a single if statement.
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
    