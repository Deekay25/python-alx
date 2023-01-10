# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

#so proud of writing this
# fhand = open('mbox-short.txt')
# domains = dict()
# for line in fhand:
#     line = line.split()
#     if len(line) < 3 or line[0] != 'From':
#         continue
#     else:
#         line_index = line[1]
#         # print(line_index)
#         domain_search= line_index.find('@')
#         domain_found = line_index[domain_search+1:]
#         print(domain_found)
#         if domain_found not in domains:
#             domains[domain_found] = 1
#         else:
#             domains[domain_found] += 1
#         # print(lines)
#         # domain_names = lines[line+1:]
#         # print(domain_names)
# print(domains)

# using .get()
fhand = open('mbox-short.txt')
domains = dict()
for line in fhand:
    if line.startswith('From '):
       line = line.split()
       line_index = line[1]
       domain_search = line_index.find('@')
       domain_found = line_index[domain_search+1:]
       if domain_found not in domains:
        domains[domain_found] = 1
       else:
        domains[domain_found] += 1
print(domains)