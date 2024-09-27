#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    Args:
        grid (list of list of int): A list of lists where 0 represents water 
        and 1 represents land. The grid is rectangular and surrounded by water.

    Returns:
        int: The perimeter of the island.
        
    The island is defined as land cells (1) connected horizontally or vertically,
    without any lakes (internal water cells surrounded by land).
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for each land cell
                perimeter += 4
                
                # Check if there is land above and subtract shared edge
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                
                # Check if there is land to the left and subtract shared edge
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
