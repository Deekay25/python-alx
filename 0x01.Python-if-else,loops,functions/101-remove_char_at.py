#!/usr/bin/python3
# a github solutio
def remove_char_at(str, n):
    new = ""
    i = 0
    for c in str:
        if i != n:
            new += c
        i += 1
    return new

print(remove_char_at("adnan", 3))

#!/usr/bin/python3
# a gitub solution
def remove_char_at(str, n):
    if 0 <= n <= len(str) - 1:
        return (str[:n] + str[n + 1:])
    return (str[:])


#my solution
#but it did not work
def remove_chat_at(str,n):
    result = ''
    for i in range(len(str)):
        if i == str[n]:
            continue
        result = result + i
    return result
print(remove_chat_at("adna n", 3))


