#!/usr/bin/python3

if __name__ == "__main__":
    records: list = []

    # using a set because it stores unique identifiers
    scoreSet: set = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name,score])
        scoreSet.add(score)
    
    # remove min, so the next value of min is the second lowest grade
    scoreSet.remove(min(scoreSet))

    records.sort()
    for item in records:
        if item[1] == min(scoreSet):
            print(item[0])
    