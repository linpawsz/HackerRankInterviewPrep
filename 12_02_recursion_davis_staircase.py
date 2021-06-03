#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n):
    # Write your code here
    steps = [1, 2, 3]
    ways = {}

    def climb(n, steps, ways):
        ret = 0
        for step in steps:
            if n - step == 0:
                ret += 1
            elif n - step > 0:
                if n - step not in ways:
                    ways[n - step] = climb(n - step, steps, ways)
                print(ways[n - step])
                ret += ways[n - step]
        return ret

    return climb(n, steps, ways)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
