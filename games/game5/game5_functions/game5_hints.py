import random
def starting_Hints(grid, min_hints=1, max_hints=3):  # Add parameters for hints
    for subgrid_row in range(3):
        for subgrid_col in range(3): 
            positions = [(row, col) for row in range(subgrid_row * 3, (subgrid_row + 1) * 3)
                         for col in range(subgrid_col * 3, (subgrid_col + 1) * 3)]
            random.shuffle(positions)
            hints = random.randint(min_hints, max_hints)  # Use the selected difficulty
            for row, col in positions[hints:]:
                grid[row][col] = 0
    return grid