# Desc: The positions of each individual grid are calculated by multiplying the subgrid row and column by 3,
# to get the starting position of the subgrid, then iterating through the next 3 rows and columns, 
# to find and get any grid position the player wants to fill. 

def init_Grid():
    return [[0] * 9 for _ in range(9)]      # Initialize a 9x9 grid with zeros, an empty Sudoku grid
