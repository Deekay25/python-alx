# 10.1. Operating System Interface
# The os module provides dozens of functions for interacting with the operating system:
import os
print(os.getcwd())

os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell

# Be sure to use the import os style instead of from os import *. 
# This will keep os.open() from shadowing the built-in open() function which operates much differently.

# Be sure to use the import os style instead of from os import *. This will keep os.open() 
# from shadowing the built-in open() function which operates much differently.
import os

dir(os) # <returns a list of all module functions>
help(os) # <returns an extensive manual page created from the module's docstrings>

# For daily file and directory management tasks, 
# the shutil module provides a higher level interface that is easier to use:

import shutil
shutil.copyfile('data.db', 'archive.db') #'archive.db'
shutil.move('/build/executables', 'installdir') # 'installdir'


# 10.2. File Wildcards

#The glob module provides a function for making file lists from directory wildcard searches:
import glob
glob.glob('*.py')

# 10.3. Command Line Arguments
# Common utility scripts often need to process command line arguments. 
# These arguments are stored in the sys module’s argv attribute as a list. 
# For instance the following output results from running python demo.py one two three at the command line:

import sys
print(sys.argv) #['demo.py', 'one', 'two', 'three']

#The argparse module provides a more sophisticated mechanism to process command line arguments. 
# The following script extracts one or more filenames and an optional number of lines to be displayed:
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

#10.4. Error Output Redirection and Program Termination
#The sys module also has attributes for stdin, stdout, and stderr. 
# The latter is useful for emitting warnings 
# and error messages to make them visible even when stdout has been redirected:
sys.stderr.write('Warning, log file not found starting a new one\n')
#the most direct way to terminate a script is to use sys.exit().

# 10.5. String Pattern Matching
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') #['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') #'cat in the hat'

#When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:
'tea for too'.replace('too', 'two') #'tea for two'

# 10.6. Mathematics

import math
math.cos(math.pi / 4)
math.log(1024, 2)

#The random module provides tools for making random selections:
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10) # sampling without replacement
random.random()
random.randrange(6)

import statistics
statistics.mean(data)
statistics.median(data)

# 10.7. Internet Access¶

