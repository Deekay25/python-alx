# you can use or list dictionaries in a list

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)


##################################################################################
# A more realistic example would involve more than three aliens with
# code that automatically generates each alien. In the following example we
# use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# # Show how many aliens have been created.
# print(f'there are {len(aliens)} created')

##################################################################################
# These aliens all have the same characteristics, but Python considers
# each one a separate object, which allows us to modify each alien
# individually.
# How might you work with a group of aliens like this? Imagine that one
# aspect of a game has some aliens changing color and moving faster as the
# game progresses. When it’s time to change colors, we can use a for loop and
# an if statement to change the color of aliens. For example, to change the
# first three aliens to yellow, medium-speed aliens worth 10 points each, we
# could do this:

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        # print(alien)
# for alien in aliens[:5]:
#     print(alien)

# print(aliens[:5],'new')


##################################################################################
# You could expand this loop by adding an elif block that turns yellow
# aliens into red, fast-moving ones worth 15 points each. Without showing the
# entire program again, that loop would look like this:

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast-moving'
        alien['points'] = 15
print(aliens[:5])

# It’s common to store a number of dictionaries in a list when each dictionary
# contains many kinds of information about one object. For example,
# you might create a dictionary for each user on a website, as we did in user.py
# on page 100, and store the individual dictionaries in a list called users. All
# of the dictionaries in the list should have an identical structure so you can
# loop through the list and work with each dictionary object in the same way.