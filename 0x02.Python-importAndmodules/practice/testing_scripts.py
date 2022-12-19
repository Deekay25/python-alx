def fib2(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


#When you run a Python module with
#python fibo.py <arguments>
#the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". 
# That means that by adding this code at the end of your module:
if __name__ == "__main__":
    import sys
    fib2(int(sys.argv[1]))

# Note: If the module is imported, the code is not run
#This is often used either to provide a convenient user interface to a module, 
# or for testing purposes (running the module as a script executes a test suite).