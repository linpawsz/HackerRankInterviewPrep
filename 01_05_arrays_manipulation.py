#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
# This HackerRank problem seems to be messed up - in the implementation - multiple of them are problematic.
#

def arrayManipulation(n, queries):
    # Write your code here
    res = [0] * (n + 1)
    for row in range(len(queries)):
        a = queries[row][0]
        b = queries[row][1]
        k = queries[row][2]
        res[a - 1] += k
        res[b] -= k
    sm = 0
    mx = 0
    for i in range(len(res)):
        sm += res[i]
        if sm > mx:
            mx = sm
    return mx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
