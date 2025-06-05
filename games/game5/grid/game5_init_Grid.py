"""
Initialize the Sudoku grid for Game 5.
"""


def init_grid():
    """
    Create and return an empty 9x9 Sudoku grid.

    Returns:
        list[list[int]]: A 9x9 grid filled with zeros.
    """
    return [[0] * 9 for _ in range(9)]
