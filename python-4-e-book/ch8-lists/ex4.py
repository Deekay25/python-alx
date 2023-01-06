# resolve exercise please

# Exercise 4: Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you
# determine that? How would you produce the list of all the words that
# Shakespeare used? Would you download all his work, read it and track
# all unique words by hand?
# Let’s use Python to achieve that instead. List all unique words, sorted
# in alphabetical order, that are stored in a file romeo.txt containing a
# subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each

# line, split the line into a list of words using the split function. For
# each word, check to see if the word is already in the list of unique
# words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words
# in alphabetical order.

# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

# open a file and read line by line
fhand = input('Enter file: ')
fopen = open(fhand)
unique_list = []
for line in fopen:
    # print(line)
# split the line into words
    line = line.split()
# for each word, check if it is already in the list of the unique words
    # print(line)
    for i in line:
        if i not in unique_list:
        # if i is not unique_list: # this way did not work
        # if i != unique_list: # this way did not work
# if word is not on the list, add it to the list
            unique_list.append(i)
# when done sort the words alphabetically and print
unique_list.sort()
print(unique_list)
# print(sorted(unique_list))
