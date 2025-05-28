import os
from utils.press_any_key import wait_for_any_key
from utils.colorama import Fore, Style

def introduction():
    Clear = lambda: os.system("cls")
    Clear()
    print(Fore.MAGENTA + "="*50 + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "Bienvenue dans le 5e mini jeu : SUDOKU !" + Style.RESET_ALL)
    print(Fore.MAGENTA + "="*50 + Style.RESET_ALL)
    print(Fore.CYAN + "Remplissez les cases vides avec des nombres de 1 à 9 sans répéter de nombre dans la même colonne, ligne ou grid 3x3." + Style.RESET_ALL)
    print(Fore.GREEN + "Commandes disponibles :" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "  1. Remplir/modifier une case" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "  2. Effacer une case" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "  3. Soumettre la grille" + Style.RESET_ALL)
    print(Fore.MAGENTA + "="*50 + Style.RESET_ALL)
    print(Fore.CYAN + "Bonne chance !" + Style.RESET_ALL)
    wait_for_any_key()