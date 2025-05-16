import random
from .game5_grid_is_valid import is_valid
def fill_Grid(grid): # Fill the grid with random numbers from 1 to 9 while enforcing Sudoku rules
    for row in range(9):
        for col in range(9):
            attempts = 0 # Attempts to avoid infinite loops where the game gets stuck in infinite loop if a number can't be placed
            while attempts < 20:
                num = random.randint(1, 9)
                if is_valid(grid, row, col, num): # Checks if the cell is already filled, if so then skip
                    grid[row][col] = num
                    break
                attempts += 1
    return grid
