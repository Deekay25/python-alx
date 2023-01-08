# Exercise 5: Minimalist Email Client.
# MBOX (mail box) is a popular file format to store and share a collection
# of emails. This was used by early email servers and desktop apps.
# Without getting into too many details, MBOX is a text file, which
# stores emails consecutively. Emails are separated by a special line which
# starts with From (notice the space). Importantly, lines starting with
# From: (notice the colon) describes the email itself and does not act as
# a separator. Imagine you wrote a minimalist email app, that lists the
# email of the senders in the user’s Inbox and counts the number of emails.
# Write a program to read through the mail box data and when you find
# line that starts with “From”, you will split the line into words using the
# split function. We are interested in who sent the message, which is the
# second word on the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:)
# lines and print out a count at the end. This is a good sample output
# with a few lines removed:
# python fromcount.py
# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# [...some output removed...]

# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

# # prompt user for a file name
# fhand = input('Enter a file: ')
# fopen = open(fhand)
# # read through the mail box data and split the lines that start with 'From '
# count = 0
# for line in fopen:
#     if line.startswith('From '):
#        line = line.split()
#        print(line)
# # retrieve the people that sent the email
#        emails = line[1]
#        count = count + 1
#     print(emails)   
# # count the number of 'From ' and print the cont
# print('There were ',count,' lines in the file with From as the first word')


#better approach
# fhand = input("Enter a file name: ")
fhand = open('mbox-short.txt')
# fopen = open(fhand)
count = 0
for line in fhand:
    word = line.split()
    if len(word) < 3 or word[0] != 'From ':
        continue
    print(word[1])
    count = count + 1
print('There were', count, 'line in the file with From as the first word')

