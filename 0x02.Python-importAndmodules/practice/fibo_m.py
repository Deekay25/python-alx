# python modules
## modules are python files that contain python functions 
## modules can be imported to used in other modules or files

## file name --> fibo.py
### to use fibo.py use "import fibo" in another file
### to access fibo use fibo.functionName()
# a module contains functions and executable statements
def fib(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


#6.1. More on Modules
