"""
Introduction for Game 4 (Trouvez l'intrus).
"""
from utils.colorama import Fore, Style
import msvcrt


def introduction():
    """
    Print the introduction and instructions for the
    'Trouvez l'intrus' mini-game.
    Wait for the user to press any key to continue.
    """
    print(
        Fore.MAGENTA + "=" * 60 + Style.RESET_ALL + "\n"
        + "🎉 " + Fore.YELLOW + Style.BRIGHT
        + "BIENVENUE DANS LE MINI JEUX TROUVEZ L'INTRUS"
        + Style.RESET_ALL + " 🎉\n"
        + Fore.MAGENTA + "=" * 60 + Style.RESET_ALL + "\n\n"
        "L'objectif est de trouver le mot intrus parmi les 4 qui "
        "seront listés.\n"
        "Vous devez trouver le mot secret en choisissant parmi les 4 mots "
        "proposés.\n\n"
        + Fore.GREEN + "Bonne chance!" + Style.RESET_ALL + "\n\n"
        + Fore.MAGENTA + "=" * 60 + Style.RESET_ALL
    )
    print("\nAppuyez sur n'importe quelle touche pour commencer...")
    msvcrt.getch()
