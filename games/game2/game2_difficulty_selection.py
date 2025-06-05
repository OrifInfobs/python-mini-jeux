"""
Difficulty selection for the random words game (Mots Aléatoires).
"""

from colorama import Fore


def difficulty_selection():
    """
    Prompt the user to select the difficulty level.
    Returns:
        str: The selected difficulty ('1', '2', or '3').
    """
    print("Choisissez une difficulté :")
    print(Fore.GREEN + "\n1. Facile (2 lettres révélées)")
    print(Fore.LIGHTYELLOW_EX + "\n2. Moyen (1 lettre révélée)")
    print(Fore.RED + "\n3. Difficile (aucune lettre révélée)")
    difficulty = input(
        "\nEntrez le numéro de la difficulté (1, 2 ou 3) : "
    ).strip()
    while difficulty not in ["1", "2", "3"]:
        print("\nChoix invalide. Veuillez entrer 1, 2 ou 3.")
        difficulty = input(
            "Entrez le numéro de la difficulté (1, 2 ou 3) : "
        ).strip()
    return difficulty
