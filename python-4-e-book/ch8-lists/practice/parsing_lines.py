# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# The program produces the following output:
# Sat
# Fri
# Fri
# Fri

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        print(line[2])

#better approach
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    print(line[2])