#!/usr/bin/python3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):

        #  *line syntax in Python is used for extended unpacking, also known as "unpacking the rest" or "splatting."
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    # retrieving the value of dictionary, which is a list
    queryList = student_marks[query_name]
    # counting the average by using buitin functions (sum() and len())
    avg = sum(queryList) / len(queryList)
    #setting precision to .2f
    formatAvg = "{:.2f}".format(avg)

    print(formatAvg)