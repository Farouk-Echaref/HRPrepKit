#!/usr/bin/python3

def merge_the_tools(string, k):

    tmp = ""
    strs: list = []
    for i in range(0, len(string)):
        if string[i] not in tmp:
            tmp += string[i]
        if ((i + 1) % k == 0):
            print(tmp)
            strs.append(tmp)
            tmp = ""
        else:
            continue

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)