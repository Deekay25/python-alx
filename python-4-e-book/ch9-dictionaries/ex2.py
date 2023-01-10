# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

# Sample Line:
    # From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
    # python dow.py
    # Enter a file name: mbox-short.txt
    # {'Fri': 20, 'Thu': 6, 'Sat': 1}

# dic = dict()
# count = 0
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
   
#     if len(words) < 3 or words[0] != 'From':
#         continue
#     else:
#         word = words[2]
#     if word not in dic:
#         dic[word] = 1
#     else:
#         dic[word] = dic[word] + 1
# print(dic)

############################################################
# with .get

days = dict()

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From '):
        day = (line.split()[2])
        days[day] = days.get(day,0) + 1
print(days)