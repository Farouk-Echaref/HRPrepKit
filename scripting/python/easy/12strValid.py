#!/usr/bin/python3

if __name__ == '__main__':
    s = input()
    
    if (any(c.isalnum() for c in s)):
        print("True")
    else:
        print("False")
    if (any(c.isalpha() for c in s)):
        print("True")
    else:
        print("False")
    if (any(c.isdigit() for c in s)):
        print("True")
    else:
        print("False")
    if (any(c.islower() for c in s)):
        print("True")
    else:
        print("False")
    if (any(c.isupper() for c in s)):
        print("True")
    else:
        print("False")