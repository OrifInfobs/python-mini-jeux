from utils.colorama import Fore, Style

def display_Grid(grid, hint_positions=None, player_moves=None, selected_row=None, selected_col=None, marker="()"):
    if hint_positions is None:
        hint_positions = set()
    if player_moves is None:
        player_moves = set()
    num_cols = 9
    cell_width = 3

    header = "   "
    for j in range(num_cols):
        header += f"{Fore.YELLOW}{str(j+1).center(cell_width)}{Style.RESET_ALL}"
        if (j + 1) % 3 == 0 and j != num_cols -1:
            header += "|"
    print(header)
    
    block = "-" * (cell_width * 3)
    sep = "   " + Fore.MAGENTA + f"{block}+{block}+{block}" + Style.RESET_ALL
    print(sep)

    for i, row in enumerate(grid):
        row_str = f"{Fore.YELLOW}{str(i+1).rjust(2)} {Style.RESET_ALL}"
        for j, num in enumerate(row):
            cell = f"{num}" if num != 0 else "."
            if selected_row == i and selected_col == j and selected_row is not None and selected_col is not None:
                left, right = marker[0], marker[1]
                visible = f"{left}{cell}{right}"
                cell_content = f"{Fore.RED}{visible}{Style.RESET_ALL}"
            elif (i, j) in hint_positions:
                visible = cell.center(cell_width)
                cell_content = f"{Fore.LIGHTCYAN_EX}{visible}{Style.RESET_ALL}"
            elif (i, j) in player_moves:
                left, right = marker[0], marker[1]
                visible = f"{left}{cell}{right}"
                cell_content = f"{Fore.RED}{visible}{Style.RESET_ALL}"
            else:
                color = Fore.GREEN if num != 0 else Fore.WHITE
                visible = cell.center(cell_width)
                cell_content = f"{color}{visible}{Style.RESET_ALL}"
            row_str += cell_content
            if (j + 1) % 3 == 0 and j != num_cols - 1:
                row_str += "|"
        print(row_str)
        if (i + 1) % 3 == 0 and i != num_cols - 1:
            print(sep)
    print()