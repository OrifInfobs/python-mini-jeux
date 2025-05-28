def is_grid_full(grid):
    for row in grid:
        if 0 in row:    # If there's a 0 in the grid then it means it's not full
            return False
    return True
