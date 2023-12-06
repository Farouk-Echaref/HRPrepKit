#!/usr/bin/python3

if __name__ == '__main__':
    N = int(input())

    # declare an empty list
    myList: list = []

    while (N > 0):
        # extended unpacking
        cmd, *args = input().split()
        if (cmd == "insert"):
            myList.insert(int(args[0]), int(args[1]))
        elif (cmd == "remove"):
            myList.remove(int(args[0]))
        elif (cmd == "append"):
            myList.append(int(args[0]))
        elif (cmd == "pop"):
            myList.pop()
        elif (cmd == "sort"):
            myList.sort()
        elif (cmd == "reverse"):
            myList.reverse()
        elif (cmd == "print"):
            print(myList)
        N -= 1
            
