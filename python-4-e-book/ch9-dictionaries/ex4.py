# redo exercise please
# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195





















# fhand = open('mbox-short.txt')
# messages = dict()
# for line in fhand:
#     message = line.split()
#     if len(message) < 3 or message[0] != 'From':
#         continue
#     else:
#         message = message[1]   
#         if message not in messages:
#             messages[message] = 1
#         else:
#             messages[message] += 1
# print(messages)

# max_msg = None
# max_count = None

# for key,val in messages.items():
#     # give me back the key that has the highes messages
#     if max_count is None or val > max_count:
#         max_msg = key
#         max_count = val
    
# print(max_msg,max_count)


# .get() method 

# fhand = open('mbox-short.txt')
# messages = dict()
# for line in fhand:
#     if line.startswith('From '):
#         message = line.split()[1]
#         messages[message] = messages.get(message, 0) + 1
# # print(messages)

# big_count = None
# big_word = None
# highest_messages = dict()
# for key,val in messages.items():
#     if big_count is None or val > big_count:
#         big_count = val
#         big_word = key
# if big_word not in highest_messages:
#     highest_messages[big_word] = big_count

# print(highest_messages)

