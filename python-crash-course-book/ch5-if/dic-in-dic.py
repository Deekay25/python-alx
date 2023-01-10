# Username: aeinstein
# Full name: Albert Einstein
# Location: Princeton
# Username: mcurie
# Full name: Marie Curie
# Location: Paris
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    }
# for username, user_info in users.items():
#     print('username: ', username)
#     for user in user_info:
#         print(f'{user}: {user_info[user]}')

#from book
for username, user_info in users.items():
    print('username: ', username)
    
    print(f"full name: {user_info['first']} {user_info['last']}")
    print(f"location: {user_info['location']}")