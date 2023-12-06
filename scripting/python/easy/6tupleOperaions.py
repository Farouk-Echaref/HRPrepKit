#!/usr/bin/python3

if __name__ == "__main__":

    tmp: list = []
    n = int(input())

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

     