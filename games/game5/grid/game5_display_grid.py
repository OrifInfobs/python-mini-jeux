from utils.colorama import Fore, Style

def display_Grid(grid, selected_row=None, selected_col=None):
    num_cols = 9
    cell_width = 3

    header = "   "                                                                  # 3 spaces for column numbers and separator
    for j in range(num_cols):
        header += f"{Fore.YELLOW}{str(j+1).center(cell_width)}{Style.RESET_ALL}"    # Center the column numbers
        if (j + 1) % 3 == 0 and j != num_cols -1:                                   # Add separator after every 3 columns
            header += "|"                                                           # Define the separator and add it to the header
    print(header)

    block = "-" * (cell_width * 3)                                                  # 3 cells per block
    sep = "   " + Fore.MAGENTA + f"{block}+{block}+{block}" + Style.RESET_ALL       # Define the separator and add it to the header
    print(sep)

    for i, row in enumerate(grid):
        row_str = f"{Fore.YELLOW}{str(i+1).rjust(2)} {Style.RESET_ALL}"             # This is the row number
        for j, num in enumerate(row): 
            cell = f"{num}" if num != 0 else "."                                    # Display 0 as a dot if the cell is empty
            if selected_row == i and selected_col == j:                             # If the cell is selected with 0 issues
                cell_content = f"{Fore.RED}[{cell}]{Style.RESET_ALL}".center(cell_width) # Display the selected cell in red
            else:
                color = Fore.GREEN if num != 0 else Fore.WHITE                      # Display the number in green if it's not empty, otherwise white
                cell_content = f"{color}{cell.center(cell_width)}{Style.RESET_ALL}" # Center the cell content
            row_str += cell_content                                                 # Add the cell content to the row string
            if (j + 1) % 3 == 0 and j != num_cols - 1:                              # Add separator after every 3 cells
                row_str += "|"                                            
        print(row_str)
        if (i + 1) % 3 == 0 and i != num_cols - 1:
            print(sep)
    print()