"""
Sudoku grid utility functions for Game 5 (Sudoku).
"""


def empty_grid():
    """
    Return an empty 9x9 Sudoku grid.

    Returns:
        list[list[int]]: An empty Sudoku grid.
    """
    return [[0 for _ in range(9)] for _ in range(9)]
