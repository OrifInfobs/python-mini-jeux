from games.game5.grid.game5_grid_is_valid import is_valid

def caseMistake(grid, row, col, number):    # Check if the guessed number is valid and update the grid accordingly
    if grid[row][col] != 0:
        print("Cette case est déjà remplie.")
        return True
    if not is_valid(grid, row, col, number):
        print("Dommage! Vous avez perdu !")
        return True
    return False
