from colorama import Fore, Style
def difficulty_selection(): # Function to select the difficulty level
    print("Choisissez une difficulté :")
    print(Fore.GREEN + "\n1. Facile (2 lettres révélées)")
    print(Fore.LIGHTYELLOW_EX + "\n2. Moyen (1 lettre révélée)")
    print(Fore.RED + "\n3. Difficile (aucune lettre révélée)")
    difficulty = input("\nEntrez le numéro de la difficulté (1, 2 ou 3) : ").strip()
    while difficulty not in ["1", "2", "3"]: # Validate difficulty input
        print("\nChoix invalide. Veuillez entrer 1, 2 ou 3.")
        difficulty = input("Entrez le numéro de la difficulté (1, 2 ou 3) : ").strip()
    return difficulty 