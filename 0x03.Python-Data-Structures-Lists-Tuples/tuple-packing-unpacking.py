usr = ('adnan',20,'M','deekay') # tuple packing

# unpacking a tuple
(name,age,sex,username) = usr
print(usr)
print(name)

def get_user_data():
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")
    
    return (user_email,user_password) # returned as tuple


# print(get_user_data())
user_email,user_password = get_user_data()
print(user_email)