from utils.colorama import Fore, Style

def display_Grid( # Display the Sudoku grid with optional highlighting for hints, player moves, and a selected cell
    grid,
    hint_positions=None,
    player_moves=None,
    selected_row=None,
    selected_col=None,
    marker="()"
):
    if hint_positions is None:         # Initialize sets if not provided
        hint_positions = set()
    if player_moves is None:
        player_moves = set()
    num_cols = 9                       # Number of columns (standard Sudoku)
    cell_width = 3                     # Width (How many characters) of each cell for alignment

    header = "   " 
    for j in range(num_cols):
        header += f"{Fore.YELLOW}{str(j+1).center(cell_width)}{Style.RESET_ALL}" # Print the column headers (1 to 9), with color and separators every 3 columns
        if (j + 1) % 3 == 0 and j != num_cols -1:
            header += "|"
    print(header)
    
    block = "-" * (cell_width * 3)     # Print the horizontal separator between blocks
    sep = "   " + Fore.MAGENTA + f"{block}+{block}+{block}" + Style.RESET_ALL
    print(sep)

    for i, row in enumerate(grid):                                              # Print each row of the grid
        row_str = f"{Fore.YELLOW}{str(i+1).rjust(2)} {Style.RESET_ALL}"         # Row label (1 to 9), colored
        for j, num in enumerate(row):
            cell = f"{num}" if num != 0 else "."                                # Show number or dot for empty

            if selected_row == i and selected_col == j and selected_row is not None and selected_col is not None:      # Highlight the selected cell (if any)
                left, right = marker[0], marker[1]
                visible = f"{left}{cell}{right}"
                cell_content = f"{Fore.RED}{visible}{Style.RESET_ALL}"

            elif (i, j) in hint_positions:                                                                             # Highlight hint positions (initial clues)
                visible = cell.center(cell_width)
                cell_content = f"{Fore.LIGHTCYAN_EX}{visible}{Style.RESET_ALL}"

            elif (i, j) in player_moves:                                                                               # Highlight player moves (cells filled by the player)
                left, right = marker[0], marker[1]
                visible = f"{left}{cell}{right}"
                cell_content = f"{Fore.RED}{visible}{Style.RESET_ALL}"

            else:
                color = Fore.GREEN if num != 0 else Fore.WHITE                                                         # Default coloring: green for filled, white for empty
                visible = cell.center(cell_width)
                cell_content = f"{color}{visible}{Style.RESET_ALL}"
            row_str += cell_content

            if (j + 1) % 3 == 0 and j != num_cols - 1:                                                                 # Add vertical separator every 3 columns (except at the end)
                row_str += "|"
        print(row_str)

        if (i + 1) % 3 == 0 and i != num_cols - 1:                                                                     # Add horizontal separator every 3 rows (except at the end)
            print(sep)
    print()                                                                                                            # Final newline for spacing