# #!/usr/bin/python3

if __name__ == '__main__':
    """print the number of and list of argument"""
    import sys
    # return the length of the argument
    if len(sys.argv[1:]) == 0:
        print(len(sys.argv[1:]), "arguments.")
    elif len(sys.argv[1:]) == 1:
        print(len(sys.argv[1:]), "argument:")
    else:
        print(len(sys.argv[1:]), "arugments:")
    # print the argument index and the argument
    for i in sys.argv[1:]:
        print("{}: {}".format(sys.argv.index(i), i))
    # my second solution for the for loop
    for i in range(len(sys.argv[1:])):
        print('{}:: {}'.format(i + 1, sys.argv[1:][i]))
#dkazem solution
#!/usr/bin/python3
# if __name__ == "__main__":
#     import sys
#     args = len(sys.argv)
#     if(args <= 1):
#         print("{} arguments.".format(args - 1))
#     elif(args == 2):
#         print("{} argument:".format(args - 1))
#     else:
#         print("{} arguments:".format(args - 1))
#     for x in range(1, args):
#         print("{}: {}".format(x, sys.argv[x]))

#maxi sotution
# #!/usr/bin/python3

# if __name__ == "__main__":
#     """Print the number of and list of arguments."""
#     import sys

#     count = len(sys.argv) - 1
#     if count == 0:
#         print("0 arguments.")
#     elif count == 1:
#         print("1 argument:")
#     else:
#         print("{} arguments:".format(count))
#     for i in range(count):
#         print("{}: {}".format(i + 1, sys.argv[i + 1]))
