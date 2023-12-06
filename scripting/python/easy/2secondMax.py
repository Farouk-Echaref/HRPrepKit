#!/usr/bin/python3

# retrieve the second max in a list
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # first method using list
    # newArr=list(arr)
    # newArr.sort()
    # newArr.reverse()

    # for i in range(len(newArr)):
    #     if newArr[i] > newArr[i + 1]:
    #         print(newArr[i + 1])
    #         break

    # second method using set and list, could fail in out of bounds
    # newSet = set(arr)
    # newList = list(newSet)
    # print(newList[len(newList) - 2])

    # set and max
    newSet = set(arr)
    newSet.remove(max(newSet))
    print(max(newSet))