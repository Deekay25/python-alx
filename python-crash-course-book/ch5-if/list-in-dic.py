# make a program with the below output


# You ordered a thick-crust pizza with the following toppings:
# mushrooms
# extra cheese

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print(f"you ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print(f"\t{topping}")

#####################################################################################
# make a program with the below output
# Jen's favorite languages are:
# Python
# Ruby
# Sarah's favorite languages are:
# C
# Phil's favorite languages are:
# Python
# Haskell
# Edward's favorite languages are:
# Ruby
# Go

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")




# To refine this program even further, you could include an if statement
# at the beginning of the dictionary’s for loop to see whether each
# person has more than one favorite language by examining the value of
# len(languages). If a person has more than one favorite, the output would
# stay the same. If the person has only one favorite language, you could
# change the wording to reflect that. For example, you could say Sarah's
# favorite language is C.



#####################################################################################
# You should not nest lists and dictionaries too deeply. If you’re nesting items much
# deeper than what you see in the preceding examples or you’re working with someone
# else’s code with significant levels of nesting, most likely a simpler way to solve the
# problem exists.