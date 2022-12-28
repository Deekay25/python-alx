"""
    when you are using a python file as module
    to avoid execution of non classes, functions and loops
    from the module use if __name__ == '__main__': property
"""
def add(a, b):
    return a + b

#returns the value main in this file
print(__name__) #returns the name of the module  used in another file 
if __name__ == '__main__': #this is regarded as an entry point in python
    print(add(1,2))