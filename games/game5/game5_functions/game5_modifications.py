from games.game5.game5_functions.game5_output_utilisateur import ask_yes_no

def modification(modifications_left):                               # Ask the user if they want to modify their input and modify counter.
    while modifications_left > 0:
        wants_modify = ask_yes_no(f"Souhaitez-vous modifier votre saisie ? (Modifications restantes : {modifications_left})")
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
        else:
            break
    return None, None, None, modifications_left

def allow_modification():                                           # Ask if the user wants to allow modifications in case of an error
    while True:
        allow_modification = ask_yes_no("Permettre les modifications en cas d'erreur ?") 
        if allow_modification:
            print("Les modifications sont autorisées pour ce jeux.")
            return True
        else:
            print("Les modifications ne sont donc pas autorisées.")
            return False