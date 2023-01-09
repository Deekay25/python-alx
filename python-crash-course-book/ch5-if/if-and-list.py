# a program checking if the list is empty first

requested_toppings = []
if requested_toppings: # checks wether the list is empty or not
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")

