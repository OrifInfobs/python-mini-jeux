from utils.colorama import Fore, Style

def display_Grid(grid): # Print the grid for the player to see
    for row_index, row in enumerate(grid):
        if row_index % 3 == 0 and row_index != 0: # Add a horizontal separator every 3 rows for readability
            print(Fore.MAGENTA + "-" * 21 + Style.RESET_ALL)
        formatted_row = (Fore.MAGENTA + " | " + Style.RESET_ALL).join(
            " ".join(
                f"{Fore.GREEN}{num}{Style.RESET_ALL}" if num != 0 else f"{Fore.WHITE}.{Style.RESET_ALL}"
                for num in row[col:col+3]
            )
            for col in range(0, 9, 3)
        )
        print(formatted_row)
    print()