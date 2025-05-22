import random
from games.game5.grid.game5_grid_is_valid import is_valid
from games.game5.grid.game5_find_empty import checkCaseAvailability

def grid_fill(grid):
    empty = checkCaseAvailability(grid)    # Find the first empty cell in the grid
    if not empty:               # If no empty cell is found, the grid is complete
        return True  
    row, col = empty            # Get the row and column of the empty cell
    nums = list(range(1, 10))   # Create a list of numbers from 1 to 9
    random.shuffle(nums)        # Shuffle the numbers to ensure randomness each game
    for num in nums:            # Iterate through the shuffled numbers
        if is_valid(grid, row, col, num):       # Check if the number can be placed in the grid without violating Sudoku rules
            grid[row][col] = num                # Place the number in the empty cell
            if grid_fill(grid):                 # Loop to call the function to fill the next empty cell until there are none left
                return True
            grid[row][col] = 0                  # If placing the number doesn't lead to a solution, reset the cell to empty
    return False                                # If no number can be placed in the empty cell, return False to backtrack
