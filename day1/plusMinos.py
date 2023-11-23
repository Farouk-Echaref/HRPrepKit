#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    nOfNeg: int = 0
    nOfPos: int = 0
    nOfZer: int = 0
    for n in arr:
        if n > 0:
            nOfPos += 1
        elif n == 0:
            nOfZer += 1
        elif n < 0 :
            nOfNeg += 1
    
    print("{:.6f}".format(nOfPos/len(arr)))
    print("{:.6f}".format(nOfNeg/len(arr)))
    print("{:.6f}".format(nOfZer/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
