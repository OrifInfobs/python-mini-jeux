def is_valid(grid, row, col, num):
    if num in grid[row] or num in [grid[r][col] for r in range(9)]: # Check if a number can be placed in the grid without violating Sudoku rules
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) # Determine the starting row and column of the 3x3 subgrid. Start_col is the first column and is repeated for the 3 columns of the subgrid. Start_row is the first row and is repeated for the 3 rows of the subgrid.
    return all(grid[r][c] != num for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)) # Check if the number is already in the 3x3 subgrid by checking through the rows and columns of the subgrid.
