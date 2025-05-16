import os
from utils.press_any_key import wait_for_any_key
from .grid.game5_init_Grid import init_Grid
from utils.colorama import Fore, Style

def introduction() :
    Clear = lambda : os.system ("cls")
    Clear()
    print(Fore.MAGENTA + "="*120 + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "Bienvenue dans le 5e mini jeu : SUDOKU !" + Style.RESET_ALL + " 🎲")
    print(Fore.MAGENTA + "="*120 + Style.RESET_ALL)
    print("Remplissez les cases vides avec des nombres de 1 à 9 sans répéter de nombre dans la même colonne, ligne ou carré 3x3.")
    print(Fore.CYAN + "Bonne chance !" + Style.RESET_ALL)
    print(Fore.MAGENTA + "="*120 + Style.RESET_ALL)
    wait_for_any_key()
    init_Grid()