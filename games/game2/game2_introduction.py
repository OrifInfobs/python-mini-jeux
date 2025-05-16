import os
from utils.colorama import Fore, Style

Clear = lambda: os.system("cls") # Clear console function

def introduction(): # Main game function and boot to game manager
    Clear()
    print(
        Fore.MAGENTA + "="*60 + Style.RESET_ALL + "\n"
        + "🎉 " + Fore.YELLOW + Style.BRIGHT + "BIENVENUE DANS LE MINI JEUX WORDLE" + Style.RESET_ALL + " 🎉\n"
        + Fore.MAGENTA + "="*60 + Style.RESET_ALL + "\n\n"
        "Devinez un mot secret de 5 lettres parmi une liste en 6 essais.\n"
        "Ces mots sont choisis aléatoirement et sont toujours des mots\n"
        "du dictionnaire valides.\n\n"
        "Voici les symboles que vous verrez dans les résultats de vos essais:\n\n"
        + Fore.GREEN + Style.BRIGHT + "✔ = Lettre correcte et bien placée" + Style.RESET_ALL + "\n"
        + Fore.RED + Style.BRIGHT + "❌ = Lettre incorrecte (non présente dans le mot)" + Style.RESET_ALL + "\n"
        + Fore.YELLOW + Style.BRIGHT + "➕ = Lettre correcte mais mal placée" + Style.RESET_ALL + "\n"
        + Fore.BLUE + Style.BRIGHT + "➖ = Lettre correcte mais toutes les occurrences ont déjà été comptées" + Style.RESET_ALL + "\n\n"
        + Fore.CYAN + "Bonne chance!" + Style.RESET_ALL + "\n"
        + Fore.MAGENTA + "="*60 + Style.RESET_ALL
    )