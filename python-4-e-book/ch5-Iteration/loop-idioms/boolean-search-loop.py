found = False
for value in [13,34,5,5,24,345,24,32,64]:
    if value == 24:
        found = True
        break
    else:
        found = False
    print(found)
print("Truth",found)