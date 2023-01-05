# make a program that can do the below

# python search6.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt


# python search6.py
# Enter the file name: mbox-short.txt
# There were 27 subject lines in mbox-short.txt

# python search7.py
# Enter the file name: na na boo boo
# File cannot be opened: na na boo boo


# 1
# fhand = input("Enter file name: ")
# fopen = open(fhand)
# count = 0
# for line in fopen:
#     count = count + 1
# print('There were', count, 'subject lines in', fhand)

# 2

# fhand = input('Enter a file name: ')
# try:
#     fopen = open(fhand)
# except:
#     print(fhand, 'cannot be opened')
#     quit()
# count = 0
# for lines in fopen:
#     count = count + 1
# print('There are', count, 'lines in', fhand)