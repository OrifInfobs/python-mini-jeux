def is_grid_full(grid):
    for row in grid:
        if 0 in row:
            return False
    return True
