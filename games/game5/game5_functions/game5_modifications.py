"""
Functions for handling modifications in Game 5 (Sudoku).
"""

from games.game5.game5_functions.game5_yes_no import ask_yes_no


def allow_modification():
    """
    Ask if the user wants to allow modifications in case of an error.
    Returns:
        bool: True if modifications are allowed, False otherwise.
    """
    while True:
        allow_mod = ask_yes_no("Permettre les modifications en cas d'erreur ?")
        if allow_mod:
            print("Les modifications sont autorisées pour ce jeu.")
            return True
        print("Les modifications ne sont donc pas autorisées.")
        return False


def modification(modifications_left):
    """
    Ask the user if they want to modify their input and get the new input
    Args:
        modifications_left (int): Number of modifications left.
    Returns:
        tuple: (row, col, num, modifications_left) or
            (None, None, None, modifications_left)
    """
    while modifications_left > 0:
        wants_modify = ask_yes_no(
            "Souhaitez-vous modifier votre saisie ? "
            f"(Modifications restantes : {modifications_left})"
        )
        if wants_modify:
            try:
                row = int(input("Numéro de ligne (1-9) : ")) - 1
                col = int(input("Numéro de colonne (1-9) : ")) - 1
                if not (0 <= row < 9 and 0 <= col < 9):
                    print("Veuillez entrer des numéros entre 1 et 9.")
                    continue
                num = int(input("Nombre à placer (1-9) : "))
                if not (1 <= num <= 9):
                    print("Veuillez entrer un nombre entre 1 et 9.")
                    continue
                modifications_left -= 1
                return row, col, num, modifications_left
            except ValueError:
                print("Entrée invalide. Veuillez entrer des chiffres valides.")
    return None, None, None, modifications_left
