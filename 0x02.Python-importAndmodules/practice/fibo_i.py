# import fibo_m # imports a module

# print(fibo_m.fib(20)) # using the functions inside a module

# print(fibo_m.__name__) # returns back the module name

# # this is done professionaly so if you want to use the function a lot
# # you save it to a variable
# fib = fibo_m.fib
# print(fib(10))



#6.1. More on Modules
#A module can contain executable statements as well as function definitions. 
# These statements are intended to initialize the module. 
# They are executed only the first time the module name is encountered in an import statement.
# modules are always advised to be imorted at the top of a file
# you can import each function from a modulbe as seen below
from fibo_m import fib, fib2 
print("udner",fib(10))


#this import everything except those names starting with _
# it is usualyy not recommended it makes code less clear
from fibo_m import *

# using the as keyword
# this makes the module fibo_m to be used as fib
import fibo_m as fib
print(fib.fib(20))

# using the as keyword with from
from fibo_m import fib as fibonacci
print(fibonacci(20))

#Note For efficiency reasons, each module is only imported once per interpreter session. 
# Therefore, if you change your modules, you must restart the interpreter – or, 
# if it’s just one module you want to test interactively, 
# use importlib.reload(), e.g. import importlib; importlib.reload(modulename).


#6.1.2. The Module Search Path
#When a module named spam is imported, the interpreter first searches for a built-in module with that name.
# These module names are listed in sys.builtin_module_names. If not found, it then searches for a 
# file named spam.py in a list of directories given by the variable sys.path. sys.path is initialized from these locations:


# 6.1.3. “Compiled” Python files
# To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc, 
# where the version encodes the format of the compiled file; it generally contains the Python version number. For example, in CPython release 3.3 
# the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc. This naming convention allows compiled modules from different 
# releases and different versions of Python to coexist.

# 6.3. The dir() Function
# The built-in function dir() is used to find out which names a module defines. 
# It returns a sorted list of strings:
import fibo_m, sys
dir(fibo_m)
#returns ['__name__', 'fib', 'fib2']
dir(sys) 
#Without arguments, dir() lists the names you have defined currently:
a = [1, 2, 3, 4, 5]
import fibo_m
fib = fibo_m.fib
dir()
#return ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
#Note that it lists all types of names: variables, modules, functions, etc.

# dir() does not list the names of built-in functions and variables.
#  If you want a list of those, they are defined in the standard module builtins:
import builtins
dir(builtins)

# 6.4. Packages
# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
#  For example, the module name A.B designates a submodule named B in a package named A. 
# Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, 
# the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

# The __init__.py files are required to make Python treat directories containing the file as packages. 
# This prevents directories with a common name, such as string, unintentionally hiding valid modules 
# that occur later on the module search path. In the simplest case, __init__.py can just be an empty file,
#  but it can also execute initialization code for the package or set the __all__ variable, described later.

import sound.effects.echo #importing packages and subpackages, submodules only
from sound.effects import echo #with this you can import variables, classes, functions, packages and modules
from sound.effects.echo import echofilter

# Note that when using from package import item, the item can be either a submodule (or subpackage) of the package,
#  or some other name defined in the package, like a function, class or variable.

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; 
# the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

# 6.4.1. Importing * From a Package
# 6.4.2. Intra-package References
# 6.4.3. Packages in Multiple Directories
# read from --> https://docs.python.org/3/tutorial/modules.html#more-on-modules

