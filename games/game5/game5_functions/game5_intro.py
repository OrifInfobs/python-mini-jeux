import os
from utils.press_any_key import wait_for_any_key
from utils.colorama import Fore, Style

"""
Introduction functions for Game 5 (Sudoku).
"""


def clear_screen():
    os.system("cls")


def introduction():
    """
    Print the introduction for the Sudoku game.
    """
    commandes = "\nCommandes Disponibles: \n"
    underlined_text = "\x1B[4m" + commandes + "\x1B[0m"
    clear_screen()
    print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)
    print(
        Fore.YELLOW + Style.BRIGHT +
        "Bienvenue dans le 5e mini jeu : SUDOKU !" +
        Style.RESET_ALL
    )
    print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)
    print(
        Fore.CYAN +
        "Remplissez les cases vides avec des nombres de 1 à 9 sans "
        "répéter de nombre dans la même colonne, ligne ou grid 3x3.\n"
        + Style.RESET_ALL
    )
    print(Fore.GREEN + underlined_text + Style.RESET_ALL)
    print(
        Fore.LIGHTYELLOW_EX +
        "  1. Remplir/modifier une case" +
        Style.RESET_ALL
    )
    print(
        Fore.LIGHTYELLOW_EX +
        "  2. Effacer une case" +
        Style.RESET_ALL
    )
    print(
        Fore.LIGHTYELLOW_EX +
        "  3. Soumettre la grille\n" +
        Style.RESET_ALL
    )
    print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)
    print(Fore.CYAN + "\nBonne chance !\n" + Style.RESET_ALL)
    print("\nAppuyez sur une touche pour commencer la partie!")
    wait_for_any_key()
