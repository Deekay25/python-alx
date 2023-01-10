# write a program that will clean the below text from a file romeo-full.txt and print the occurrence of words
# But, soft! what light through yonder window breaks?
# It is the east, and Juliet is the sun.
# Arise, fair sun, and kill the envious moon,
# Who is already sick and pale with grief,

# {'swearst': 1, 'all': 6, 'afeard': 1, 'leave': 2, 'these': 2,
# 'kinsmen': 2, 'what': 11, 'thinkst': 1, 'love': 24, 'cloak': 1,
# a': 24, 'orchard': 2, 'light': 5, 'lovers': 2, 'romeo': 40,
# 'maiden': 1, 'whiteupturned': 1, 'juliet': 32, 'gentleman': 1,
# 'it': 22, 'leans': 1, 'canst': 1, 'having': 1, ...}
import string

# fhand = input('Enter file: ')
# try:
#     fopen = open(fhand)
# except:
#     print('no such file')
#     exit()
# dic = dict()
# for line in fopen:
#     # cleaning the file
#     line = line.rstrip()
#     line = line.translate(line.maketrans('','',string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in dic:
#             dic[word] = 1
#         else:
#             dic[word] = dic[word] + 1
# print((dic))


fhand = input('Enter file: ')
try:
    fopen = open(fhand)
except:
    print('no such file')
    exit()
dic = dict()
for line in fopen:
    # cleaning the file
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1
print((dic))
    