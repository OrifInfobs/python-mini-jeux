def contains_zugzug_date(grid):
    date_seq = [1, 5, 1, 1, 1, 9, 9, 4]
    for row in grid:
        for i in range(len(row) - len(date_seq) + 1):
            if row[i:i+len(date_seq)] == date_seq:
                return True
    num_cols = len(grid[0]) if grid else 0
    num_rows = len(grid)
    for col in range(num_cols):
        col_vals = [grid[row][col] for row in range(num_rows)]
        for i in range(len(col_vals) - len(date_seq) + 1):
            if col_vals[i:i+len(date_seq)] == date_seq:
                return True
    return False


def zugzug_hint_counter(grid):
    """
    Counts the number of partial ZugZug hints (first 4 digits of the sequence) in the grid.
    """
    date_seq = [1, 5, 1, 1, 1, 9, 9, 4]
    count = 0
    for row in grid:
        for i in range(len(row) - 3):
            if row[i:i+4] == date_seq[:4]:
                count += 1
    num_cols = len(grid[0]) if grid else 0
    num_rows = len(grid)
    for col in range(num_cols):
        col_vals = [grid[row][col] for row in range(num_rows)]
        for i in range(len(col_vals) - 3):
            if col_vals[i:i+4] == date_seq[:4]:
                count += 1
    return count
