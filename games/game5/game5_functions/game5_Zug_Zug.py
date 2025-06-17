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
