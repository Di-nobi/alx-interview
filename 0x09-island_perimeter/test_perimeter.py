#!/usr/bin/python3

def test_perimeter(grid):
    if not grid:
        return
    perimeter = 0
    for row in grid:
        for i in range(len(row)):
            cell = row[i]
            if cell == 1:
                perimeter += 4
                # Check left neighbor
                if i > 0 and row[i - 1] == 1:
                    perimeter -= 2