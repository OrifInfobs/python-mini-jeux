from utils.input_handler import get_valid_input


def select_difficulty():
    print("\nChoisissez une difficulté pour le Sudoku :")
    print("1. Facile (4-6 chiffres révélés par sous-grille)")
    print("2. Moyen (2-4 chiffres révélés par sous-grille)")
    print("3. Difficile (1-2 chiffres révélés par sous-grille)")
    choice = get_valid_input("Votre choix (1/2/3) : ", ["1", "2", "3"])
    if choice == "1":
        return (4, 6)
    elif choice == "2":
        return (2, 4)
    else:
        return (1, 2)
