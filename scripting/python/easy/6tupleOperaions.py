#!/usr/bin/python3

if __name__ == "__main__":

    tmp: list = []
    n = int(input())

    # map() function returns a map object(which is an iterator) of the results after applying 
    # touthe given function to each item of a given iterable (list, tuple etc.) 
    # read and store in a dict
    # M = map(int,input().split())

    # t = tuple(M)
    num = input().split()
    i: int = 0
    while (i < n):
        tmp.append(int(num[i]))
        i += 1
    myTuple: tuple = tuple(tmp)
    hashed = hash(myTuple)
    print(hashed)

     