"""
Functions to fill the Sudoku grid for Game 5.
"""

import random
from games.game5.grid.game5_grid_is_valid import is_valid
from games.game5.grid.game5_find_empty import find_empty


def grid_fill(grid):
    """
    Recursively fill the Sudoku grid using backtracking.

    Args:
        grid (list[list[int]]): The Sudoku grid.

    Returns:
        bool: True if the grid is filled, False otherwise.
    """
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if grid_fill(grid):
                return True
            grid[row][col] = 0
    return False
