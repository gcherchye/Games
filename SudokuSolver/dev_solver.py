"""Main dev file"""
from __future__ import absolute_import

import numpy as np


GRID = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 3, 4, 5, 6, 7],
        [0, 0, 4, 5, 0, 6, 1, 8, 2],
        [0, 0, 1, 0, 5, 8, 2, 0, 6],
        [0, 0, 8, 0, 0, 0, 0, 0, 1],
        [0, 2, 0, 0, 0, 7, 0, 5, 0],
        [0, 0, 0, 7, 0, 5, 0, 2, 8],
        [0, 8, 0, 0, 6, 0, 7, 0, 0],
        [0, 0, 7, 0, 8, 3, 0, 1, 0]]

def possible(y, x, n):
    global GRID

    # Check on the row
    for i in range(0, 9):
        if GRID[y][i] == n:
            return False
    
    # Check on the column
    for i in range(0, 9):
        if GRID[i][x] == n:
            return False

    # Check on the square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0 ,3):
        for j in range(0, 3):
            if GRID[y0+i][x0+j] == n:
                return False

    return True

def solve():
    global GRID

    for y in range(9):
        for x in range (9):
            if GRID[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        GRID[y][x] = n
                        solve()
                        yield from solve()
                        GRID[y][x] = 0
                
                return
    
    yield np.matrix(GRID)
