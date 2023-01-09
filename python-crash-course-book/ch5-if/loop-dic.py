user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

#best way to do it
for key, value in user_0.items():
    print(key, value)

# practicing
for v in user_0:
    print(v,user_0[v])

#sorting a dictionary
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")