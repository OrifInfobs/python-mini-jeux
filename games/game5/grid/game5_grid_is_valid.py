"""
Validation functions for the Sudoku grid in Game 5.
"""


def is_valid(grid, row, col, num):
    """
    Check if placing num at (row, col) is valid in the Sudoku grid.
    Args:
        grid (list[list[int]]): The Sudoku grid.
        row (int): Row index.
        col (int): Column index.
        num (int): Number to check.
    Returns:
        bool: True if valid, False otherwise.
    """
    if num in grid[row] or num in [grid[r][col] for r in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    return all(
        grid[r][c] != num
        for r in range(start_row, start_row + 3)
        for c in range(start_col, start_col + 3)
    )
