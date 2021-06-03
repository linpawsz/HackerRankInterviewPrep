#!/bin/python3

import math
import os
import random
import re
import sys

# Figure out what this program means

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def digit_sum(x):
    return str(sum((int(i) for i in list(x))))


def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit(digit_sum(x))


def superDigit(n, k):
    # Write your code here
    a = digit_sum(n)
    return sup_digit(str(int(a) * k))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
