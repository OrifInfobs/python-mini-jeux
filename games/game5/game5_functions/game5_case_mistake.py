"""
Check for mistakes when filling a cell in the Sudoku grid for Game 5.
"""

from games.game5.grid.game5_grid_is_valid import is_valid


def case_mistake(grid, row, col, number):
    """
    Check if the guessed number is valid and update the grid accordingly.

    Args:
        grid (list[list[int]]): The Sudoku grid.
        row (int): Row index.
        col (int): Column index.
        number (int): Number to check.

    Returns:
        bool: True if there is a mistake, False otherwise.
    """
    if grid[row][col] != 0:
        print("Cette case est déjà remplie.")
        return True
    if not is_valid(grid, row, col, number):
        print("Dommage! Vous avez perdu !")
        return True
    return False
