# #!/usr/bin/python3
if __name__ == "__main__":
    """addition of arguments"""
    import sys
    total = 0
    for i in range(len(sys.argv[1:])):
        """loop through the arguments"""
        total = total + int(sys.argv[1:][i])
    print(total)
