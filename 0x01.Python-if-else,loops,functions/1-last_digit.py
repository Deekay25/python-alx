# #!/usr/bin/python3
# import random
# number = random.randint(-10000, 10000)
# if int(str(number)[-1]) > 5:
#     print("Last digit of", number, "is", int(str(number)[-1]), "and is greater than 5")
# elif int(str(number)[-1]) == 0:
#     print("Last digit of", number, "is", int(str(number)[-1]), "and is 0")
# else: 
#     print("Last digit of", number, "is", int(str(number)[-1]), "and is less than 6 and not 0")


#alx solution
#!/usr/bin/python3
import random 
number = random.randint(-10000, 10000)

if number < 0:
    remainder = number % -10
else:
    remainder = number % 10
print("Last digit of", number, "is", remainder)
if remainder > 5:
    print("and is greater than 5")
elif remainder == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")


#!/usr/bin/python3