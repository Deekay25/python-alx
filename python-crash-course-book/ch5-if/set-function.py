favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for lan in set(favorite_languages.values()):
    print(lan)

#very importnant
# You can build a set directly using braces and separating the elements with commas:

# >>> languages = {'python', 'ruby', 'python', 'c'}
# >>> languages
# {'ruby', 'python', 'c'}

# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
# When you see braces but no key-value pairs, you’re probably looking at a set. Unlike
# lists and dictionaries, sets do not retain items in any specific order.