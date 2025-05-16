from utils.colorama import Fore, Style

def introduction():
    print(
        Fore.MAGENTA + "="*60 + Style.RESET_ALL + "\n"
        + "🎉 " + Fore.YELLOW + Style.BRIGHT + "BIENVENUE DANS LE MINI JEUX TROUVEZ L'INTRUS" + Style.RESET_ALL + " 🎉\n"
        + Fore.MAGENTA + "="*60 + Style.RESET_ALL + "\n\n"
        "L'objectif est de trouver le mot intrus parmi les 4 qui seront listés.\n"
        "Vous devez trouver le mot secret en choisissant parmi les 4 mots proposés.\n\n"
        + Fore.CYAN + "Bonne chance!" + Style.RESET_ALL + "\n\n"
        + Fore.MAGENTA + "="*60 + Style.RESET_ALL
    )