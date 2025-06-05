"""
Functions to find empty cells in the Sudoku grid for Game 5 (Sudoku).
"""


def find_empty(grid):
    """
    Find the first empty cell (with value 0) in the Sudoku grid.

    Args:
        grid (list[list[int]]): The Sudoku grid.

    Returns:
        tuple[int, int] | None: The (row, col) of the first empty cell.
    """
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 0:
                return i, j
    return None
