# Fyi This file contains the main code for the grid of game 5 
# R = Row and C = Column as ref in file
# # Desc: The positions of each individual grid are calculated by multiplying the subgrid row and column by 3 to get the starting position of the subgrid, then iterating through the next 3 rows and columns to find and get any grid position the player wants to fill. 

import random

def init_Grid():
    return [[0] * 9 for _ in range(9)] # Initialize a 9x9 grid with zeros, an empty Sudoku grid
def display_Grid(grid): # Print the grid for the player to see
    for row_index, row in enumerate(grid):
        if row_index % 3 == 0 and row_index != 0: # Add a horizontal separator every 3 rows for readability
            print("-" * 21)
        formatted_row = " | ".join(  # Format the row with vertical separators every 3 columns
            " ".join(str(num) if num != 0 else "." for num in row[col:col+3])
            for col in range(0, 9, 3)
        )
        print(formatted_row) # Show the sudoku grid with the numbers and dots for empty spaces
    print()
def is_valid(grid, row, col, num):
    if num in grid[row] or num in [grid[r][col] for r in range(9)]: # Check if a number can be placed in the grid without violating Sudoku rules
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) # Determine the starting row and column of the 3x3 subgrid. Start_col is the first column and is repeated for the 3 columns of the subgrid. Start_row is the first row and is repeated for the 3 rows of the subgrid.
    return all(grid[r][c] != num for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)) # Check if the number is already in the 3x3 subgrid by checking through the rows and columns of the subgrid.
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
def update_Grid(grid, row, col, num): # Update the grid with the player's guess if it's valid
    if is_valid(grid, row, col, num):
        grid[row][col] = num
        return True
    return False