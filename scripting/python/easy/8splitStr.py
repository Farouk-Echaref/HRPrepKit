#!/usr/bin/python3

def split_and_join(line):
    # write your code here
    strList = line.split(" ")
    # joing string by delimiter
    strList = "-".join(strList)
    return (strList)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)