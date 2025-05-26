import os
from utils.press_any_key import wait_for_any_key
from utils.colorama import Fore, Style

def introduction():
    Clear = lambda: os.system("cls")
    Clear()
    print(Fore.MAGENTA + "="*120 + Style.RESET_ALL)         # Print a separator line
    print(Fore.YELLOW + Style.BRIGHT + "Bienvenue dans le 5e mini jeu : SUDOKU !" + Style.RESET_ALL + " 🎲")        # Intro message with colors and style
    print(Fore.MAGENTA + "="*120 + Style.RESET_ALL)         # Print another separator line
    print("Remplissez les cases vides avec des nombres de 1 à 9 sans répéter de nombre dans la même colonne, ligne ou carré 3x3.") # Game rules explanation
    print(Fore.CYAN + "Bonne chance !" + Style.RESET_ALL)
    print(Fore.MAGENTA + "="*120 + Style.RESET_ALL)         # Print a final separator line
    print(
        Fore.LIGHTYELLOW_EX +                               # Instructions on how to select grid cells
        "\nPour placer un nombre, indiquez d'abord le numéro de la ligne (1-9), puis le numéro de la colonne (1-9), puis le nombre à placer (1-9).\n"
        "Les numéros de lignes sont affichés à gauche, les numéros de colonnes en haut de la grille.\n" + Style.RESET_ALL
    )
    wait_for_any_key()