# write a program that counts each word and number of occurence from a file called romeo.txt 
# and save it to a dictionary

fhand = open('romeo.txt')
dic = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] = dic[word] + 1
print((dic))

