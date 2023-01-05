# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

fhand = input('Enter a file name: ')
fopen = open(fhand)
count = 0
sum = 0
for line in fopen:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        line_search = line.find(' ') # before I used line.find(':'), the program works correct but using (' ') is better
        line_found = line[line_search + 1:]
        # print(repr(line_found)) // very important line, the repr show there is a space when i use line.find(':')
        sum = sum + float(line_found)
        count = count + 1
print(sum/count)