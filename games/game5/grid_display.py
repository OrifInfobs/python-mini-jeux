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
