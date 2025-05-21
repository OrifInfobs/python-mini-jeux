def find_empty(grid):           # Empty space = 0
    for i in range(9):          # Iterate for each row
        for j in range(9):      # Iterate for each column
            if grid[i][j] == 0: # Check index of both row and column as to determine if the space is empty.
                return (i, j)   # Return the coordinates of the first empty space found
    return None                 # If no empty space is found, return None