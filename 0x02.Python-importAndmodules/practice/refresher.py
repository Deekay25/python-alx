#!/usr/bin/python3

""" prints the number of and the list of its arguments"""
import sys

# guillaume@ubuntu:~/0x02$ ./2-args.py 
# 0 arguments.
# guillaume@ubuntu:~/0x02$ ./2-args.py Hello
# 1 argument:
# 1: Hello
# guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
# 6 arguments:
# 1: Hello
# 2: Welcome
# 3: To
# 4: The
# 5: Best
# 6: School
# guillaume@ubuntu:~/0x02$ 

# reads the command line arguments then return it's number
# if argument is 0 return 0 arguments.
# if argument is 1 return 1 argument: then the argument
# if arguments then it will retun number of arguments then the argument starting from one

# if len(sys.argv[1:]) == 0:
#     print('{} argument.'.format(len(sys.argv[1:])))
# elif len(sys.argv[1:]) == 1:
#     print('{} argument:'.format(len(sys.argv[:1])))
# else:
#     print('{} arguments:'.format(len(sys.argv[1:])))

# for i in range(len(sys.argv[1:])):
#     print('{}: {}'.format(i+1,sys.argv[1:][i]))


