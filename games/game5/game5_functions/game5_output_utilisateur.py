"""
Functions for user output in Game 5 (Sudoku).
"""

import os
from colorama import Fore, Style

from games.game5.grid.game5_display_grid import display_Grid
from games.game5.game5_functions.game5_yes_no import ask_yes_no


def clear_console():
    """
    Clear the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def user_output(grid, hint_positions, player_moves):
    """
    Main user interaction loop for the Sudoku game.
    Handles display, input, and error messages.

    Args:
        grid (list[list[int]]): The Sudoku grid.
        hint_positions (set[tuple[int, int]]): Positions of initial clues.
        player_moves (set[tuple[int, int]]): Positions filled by the player.

    Returns:
        str: 'submit' if the user chooses to submit the grid.
    """
    last_message = ""
    while True:
        clear_console()
        if last_message:
            print(Fore.RED + last_message + Style.RESET_ALL)
            print()
            last_message = ""
        print(Fore.MAGENTA + "\n" + "=" * 40 + Style.RESET_ALL)
        print(
            Fore.YELLOW + Style.BRIGHT +
            "\nVotre grille actuelle :\n" + Style.RESET_ALL
        )
        display_Grid(grid, hint_positions, player_moves)
        print(Fore.MAGENTA + "=" * 40 + Style.RESET_ALL)
        print(Fore.CYAN + "\nQue souhaitez-vous faire ?\n" + Style.RESET_ALL)
        print(Fore.GREEN + "  1. Remplir/modifier une case\n")
        print(Fore.GREEN + "  2. Effacer une case\n")
        print(Fore.GREEN + "  3. Soumettre la grille\n" + Style.RESET_ALL)
        prompt = (
            Fore.LIGHTYELLOW_EX + "\nVotre choix (1/2/3) : " + Style.RESET_ALL
        )
        choice = input(prompt).strip()
        if choice == "1":
            try:
                row = int(input("Numéro de ligne (1-9) : ")) - 1
                col = int(input("Numéro de colonne (1-9) : ")) - 1
                if (row, col) in hint_positions:
                    last_message = (
                        "Vous ne pouvez pas modifier une case d'indice "
                        "initiale !"
                    )
                    continue

                num = int(input("Nombre à placer (1-9) : "))
                if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                    grid[row][col] = num
                    player_moves.add((row, col))
                else:
                    last_message = "Entrée hors limites."
            except ValueError:
                last_message = "Entrée invalide."
        elif choice == "2":
            try:
                row = int(input("Numéro de ligne (1-9) à effacer : ")) - 1
                col = int(input("Numéro de colonne (1-9) à effacer : ")) - 1
                if (row, col) in hint_positions:
                    last_message = (
                        "Vous ne pouvez pas effacer une case indice initial !"
                    )
                    continue
                if 0 <= row < 9 and 0 <= col < 9:
                    grid[row][col] = 0
                    player_moves.discard((row, col))
                else:
                    last_message = "Entrée hors limites."
            except ValueError:
                last_message = "Entrée invalide."
        elif choice == "3":
            confirm = ask_yes_no("Voulez-vous soumettre la grille ?")
            if confirm:
                return "submit"
        else:
            last_message = "Choix invalide."
