"""
Grid update functions for Game 5 (Sudoku).
"""

from games.game5.grid.game5_grid_is_valid import is_valid


def update_grid(grid, row, col, num):
    """
    Update the grid at the specified row and column with the given number.

    Args:
        grid (list[list[int]]): The Sudoku grid.
        row (int): Row index.
        col (int): Column index.
        num (int): Number to place.

    Returns:
        bool: True if the grid was updated, False otherwise.
    """
    if is_valid(grid, row, col, num):
        grid[row][col] = num
        return True
    return False
