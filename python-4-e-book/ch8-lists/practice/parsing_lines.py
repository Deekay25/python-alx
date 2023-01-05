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

# solution to above fail
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.split()
    # print('debug',line)
    if len(line) == 0 : continue
    if line[0] != 'From': continue
    print(line[2])