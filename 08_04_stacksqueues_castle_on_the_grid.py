#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#


# What in the holy fuck does this code do - figure it out!! Yikes!!!

def add_to_queue(mat, grid, queue, d, old_dir, i, j, new_dir):
    dist = d if old_dir==new_dir else d+1
    if dist < mat[i][j]:
        queue.append([dist, i, j, new_dir])
        mat[i][j] = dist


def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    # Matrix to store distance from starting point
    mat = [[math.inf for _ in range(n)] for __ in range(n)]
    queue = [[0, startX, startY, 'E']]
    start = 0
    i, j = startX, startY
    mat[i][j] = 0
    while i!=goalX or j!=goalY:
        d, i, j, drn = queue[start]
        start += 1
        p = i+1
        while p<n and grid[p][j]=='.':
            add_to_queue(mat, grid, queue, d, drn, p, j, 'U')
            p += 1
        p = j+1
        while p<n and grid[i][p]=='.':
            add_to_queue(mat, grid, queue, d, drn, i, p, 'L')
            p += 1
        p = i-1
        while p>=0 and grid[p][j]=='.':
            add_to_queue(mat, grid, queue, d, drn, p, j, 'D')
            p -= 1
        p = j-1
        while p>=0 and grid[i][p]=='.':
            add_to_queue(mat, grid, queue, d, drn, i, p, 'R')
            p -= 1
    return mat[goalX][goalY]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
