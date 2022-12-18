import fibo_m # imports a module

print(fibo_m.fib(20)) # using the functions inside a module

print(fibo_m.__name__) # returns back the module name

# this is done professionaly so if you want to use the function a lot
# you save it to a variable
fib = fibo_m.fib
print(fib(10))