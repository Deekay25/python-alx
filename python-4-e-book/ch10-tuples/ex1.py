# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

# so proud did it myself
fhand = open('mbox.txt')
messages = dict()
for line in fhand:
    if line.startswith('From '):
        message = line.split()[1]
        messages[message] = messages.get(message, 0) + 1

list_of_msgs = list()
for email,count in messages.items():
    list_of_msgs.append((count,email))

list_of_msgs.sort(reverse=True)

email_count = None
counts = None
for count,email in list_of_msgs:
    if counts is None or count > counts:
        counts = count
        email_count = email

print(email_count, counts)
