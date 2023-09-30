#!/usr/bin/python3
"""Island perimeter task"""

def island_perimeter(grid):
    """Gets the perimeter og a cell in a grid"""
    if not grid:
        return 
    sum = 0

    for x in (len(grid)):
        for y in (len(grid[0])):
            if grid[x][y] == 1:
                sum += 4
                if x > 0 and grid[x - 1][y] == 1:
                    sum -= 2
                if y > 0 and grid[x][y - 1] == 1:
                    sum -= 2
    return sum