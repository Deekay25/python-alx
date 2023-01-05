# 1) write a program to count the lines in a file

# 2) write a programwith following output
# From: stephen.marquard@uct.ac.za

# From: louis@media.berkeley.edu

# From: zqian@umich.edu

# From: rjlowe@iupui.edu

# 3) When this program runs, we get the following output:
# From: stephen.marquard@uct.ac.za
# From: louis@media.berkeley.edu
# From: zqian@umich.edu
# From: rjlowe@iupui.edu
# From: zqian@umich.edu
# From: rjlowe@iupui.edu
# From: cwen@iupui.edu

# 1
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print(count)

# 2
# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

# 3

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

#4 printing a particular university email from file

# fhand = open('mbox-short.txt')

# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1:
#     # if not '@uct.ac.za' in line:
#         continue
#     print(line)

