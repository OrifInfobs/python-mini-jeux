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
        "✔ = Lettre correcte et bien placée""\n"
        "❌ = Lettre incorrecte (non présente dans le mot)""\n"
        "➕ = Lettre correcte mais mal placée""\n"
        "➖ = Lettre correcte mais toutes les occurrences ont déjà été comptées""\n\n"
        "Bonne chance!""\n"
    )