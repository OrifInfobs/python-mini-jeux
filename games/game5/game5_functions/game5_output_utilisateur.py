from games.game5.game5_functions.game5_case_mistake import caseMistake
from games.game5.grid.game5_display_grid import display_Grid
from games.game5.game5_functions.game5_modifications import modification
from games.game5.game5_functions.game5_yes_no import ask_yes_no

def userOutput(grid):                                                               # Function to get user inputs for the Sudoku game
    modifications_left = 3
    while True:
        print("\nVoici la grille actuelle :")
        display_Grid(grid)
        try:
            selectRow = int(input("Numéro de ligne (1-9) : ")) - 1                  # select row
            selectColumn = int(input("Numéro de colonne (1-9) : ")) - 1             # select column
            if not (0 <= selectRow < 9 and 0 <= selectColumn < 9):                  # Check if the row and column are valid
                print("Veuillez entrer des numéros entre 1 et 9.") 
                continue
            enterNumber = int(input("Nombre à placer (1-9) : "))                    # select number
            if not (1 <= enterNumber <= 9):
                print("Veuillez entrer un nombre entre 1 et 9.")                    # Check if the number is valid
                continue

            if caseMistake(grid, selectRow, selectColumn, enterNumber):             # Check if the number is already in the row, column, or subgrid
                return None, None, None

            while modifications_left > 0:                                            # Ask the user if they want to modify their input and modify counter
                mod_row, mod_col, mod_num, modifications_left = modification(modifications_left) # Get the modified row, column, and number
                if mod_row is not None:
                    selectRow, selectColumn, enterNumber = mod_row, mod_col, mod_num # Update the selected row, column, and number
                    if caseMistake(grid, selectRow, selectColumn, enterNumber):      # Check if the modified number is already in the row, column, or subgrid
                        return None, None, None
                else:
                    break
            if selectRow is not None and selectColumn is not None:                   # If the row, column and number are valid
                confirm = ask_yes_no(f"Confirmer l'entrée {enterNumber} en ligne {selectRow+1}, colonne {selectColumn+1} ?")        # Ask for confirmation
                if confirm:
                    grid[selectRow][selectColumn] = enterNumber
                    return selectRow, selectColumn, enterNumber
            else:
                print("Ligne ou colonne non définie, saisie annulée.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer des chiffres valides.")