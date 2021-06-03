#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    inverse_position_dict = {}
    position = 0
    temp_var = 0
    swap = 0
    for pos, val in enumerate(arr):
        inverse_position_dict[val] = pos

    print(inverse_position_dict)
    print(arr)

    for i in range(len(arr)):
        if arr[i] != i + 1:
            temp_var = arr[i]
            arr[i] = i + 1
            arr[inverse_position_dict[arr[i]]] = temp_var
            inverse_position_dict[temp_var] = inverse_position_dict[arr[i]]
            swap += 1

    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
