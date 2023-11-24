#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minSum: int = 0
    maxSum: int = 0
    for n in arr:
            maxSum += n
    
    minSum = maxSum - max(arr)
    maxSum = maxSum - min(arr)
    print(minSum,maxSum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
