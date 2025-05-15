import random
def starting_Hints(grid): # Remove numbers from the grid, leaving 1-3 numbers in each 3x3 subgrid as hints
    for subgrid_row in range(3):
        for subgrid_col in range(3): 
            positions = [(row, col) for row in range(subgrid_row * 3, (subgrid_row + 1) * 3) # Get the positions of the cells in the current 3x3 subgrid
                         for col in range(subgrid_col * 3, (subgrid_col + 1) * 3)]
            random.shuffle(positions) # Shuffle the positions to randomize which numbers to remove so each game is different
            hints = random.randint(1, 3) # The random.randint(1, 3) function is used to determine how many numbers to remove from the subgrid, between 1 and 3.
            for row, col in positions[hints:]:
                grid[row][col] = 0
    return grid
