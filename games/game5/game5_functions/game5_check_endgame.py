"""
Check if the Sudoku game has ended for Game 5.
"""

from games.game5.grid.game5_grid_is_valid import is_valid


def result(grid):
    """
    Check if the Sudoku grid is complete and valid.

    Args:
        grid (list[list[int]]): The Sudoku grid.

    Returns:
        bool: True if the game is over (correct solution), False if incomplete.
    """
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num == 0:
                return False
            grid[row][col] = 0
            if not is_valid(grid, row, col, num):
                grid[row][col] = num
                return True
            grid[row][col] = num
    return False
