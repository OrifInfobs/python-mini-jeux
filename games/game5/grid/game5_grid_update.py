from games.game5.grid.game5_grid_is_valid import is_valid
def update_Grid(grid, row, col, num): # Update the grid with the player's guess if it's valid
    if is_valid(grid, row, col, num):
        grid[row][col] = num
        return True
    return False