#!/usr/bin/python3

def count_substring(string, sub_string):
    count = 0
    index = 0
    i = 0
    while (i < len(string)):
        index = string.find(sub_string, i)
        if (index < 0):
            break 
        count += 1
        i = index + 1
    return (count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)