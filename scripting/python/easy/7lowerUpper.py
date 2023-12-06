#!/usr/bin/python3

def swap_case(s):

    # method 1
    newStr = ""
    for c in s:
        if c.islower():
            newStr += c.upper() 
        else:
            newStr += c.lower()
    return (newStr)

    #method 2
    # return (s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)