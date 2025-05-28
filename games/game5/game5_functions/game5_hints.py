import random
def starting_Hints(grid, min_hints=1, max_hints=3):
    hint_positions = set()                              # Hint positions are defined as part of a set as to maintain sudoku rules
    for subgrid_row in range(3):
        for subgrid_col in range(3):                    # Start loop so it applies to every grid until none are found
            positions = [(row, col) for row in range(subgrid_row * 3, (subgrid_row + 1) * 3)   # Define the positions possible for the loop
                         for col in range(subgrid_col * 3, (subgrid_col + 1) * 3)]
            random.shuffle(positions)
            hints = random.randint(min_hints, max_hints)
            for idx, (row, col) in enumerate(positions):
                if idx < hints:
                    hint_positions.add((row, col))
                else:
                    grid[row][col] = 0
    return grid, hint_positions