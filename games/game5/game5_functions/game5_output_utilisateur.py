from games.game5.game5_functions.game5_case_mistake import caseMistake
from games.game5.grid.game5_display_grid import display_Grid
from games.game5.game5_functions.game5_modifications import modification

def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (Oui/Non) : ").strip().lower()
        if answer in ["oui", "o"]:
            return True
        elif answer in ["non", "n"]:
            return False
        else:
            print("Veuillez répondre par Oui ou Non.")

def userOutput(grid):
    modifications_left = 3
    while True:
        print("\nVoici la grille actuelle :")
        display_Grid(grid)
        try:
            selectRow = int(input("Numéro de ligne (1-9) : ")) - 1
            selectColumn = int(input("Numéro de colonne (1-9) : ")) - 1
            if not (0 <= selectRow < 9 and 0 <= selectColumn < 9):
                print("Veuillez entrer des numéros entre 1 et 9.")
                continue
            enterNumber = int(input("Nombre à placer (1-9) : "))
            if not (1 <= enterNumber <= 9):
                print("Veuillez entrer un nombre entre 1 et 9.")
                continue

            if caseMistake(grid, selectRow, selectColumn, enterNumber):
                return None, None, None

            while modifications_left > 0:
                mod_row, mod_col, mod_num, modifications_left = modification(modifications_left)
                if mod_row is not None:
                    selectRow, selectColumn, enterNumber = mod_row, mod_col, mod_num
                    if caseMistake(grid, selectRow, selectColumn, enterNumber):
                        return None, None, None
                else:
                    break
            if selectRow is not None and selectColumn is not None:
                confirm = ask_yes_no(f"Confirmer l'entrée {enterNumber} en ligne {selectRow+1}, colonne {selectColumn+1} ?")
                if confirm:
                    grid[selectRow][selectColumn] = enterNumber
                    return selectRow, selectColumn, enterNumber
            else:
                print("Ligne ou colonne non définie, saisie annulée.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer des chiffres valides.")