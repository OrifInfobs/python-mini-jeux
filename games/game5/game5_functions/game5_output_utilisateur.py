from games.game5.grid.game5_grid_is_valid import is_valid
from games.game5.grid.game5_display_grid import display_Grid

def ask_yes_no(prompt):                                                # Ask for yes or no from the user
    while True:
        answer = input(prompt + " (Oui/Non) : ").strip().lower()
        if answer in ["oui", "o"]:
            return True
        elif answer in ["non", "n"]:
            return False
        else:
            print("Veuillez répondre par Oui ou Non.")

def userOutput(grid):
    allow_modification = ask_yes_no("Permettre les modifications en cas d'erreur ?")    # Ask if the user wants to allow modifications in case of an error
    last_move = None
    while True:
        print("\nVoici la grille actuelle :")
        display_Grid(grid)
        try:
            row = int(input("Numéro de ligne (1-9) : ")) - 1           # Convert to 0-indexed as to not crash the whole system
            col = int(input("Numéro de colonne (1-9) : ")) - 1
            if not (0 <= row < 9 and 0 <= col < 9):                    # Check if the input is valid
                print("Veuillez entrer des numéros entre 1 et 9.")
                continue
            display_Grid(grid)                                         # Display the grid with the selected cell marked
            num = int(input("Nombre à placer (1-9) : "))               # Ask the user for the number to place
            if not (1 <= num <= 9):                                    # Check if the number is valid
                print("Veuillez entrer un nombre entre 1 et 9.")
                continue
            if grid[row][col] != 0 and not allow_modification:         # Check if the cell is already filled if allow modifications is not enabled
                print("Cette case est déjà remplie.")
                continue
            if not is_valid(grid, row, col, num):                      # If the number is not valid, check if the number can be placed in the grid
                print("Ce nombre ne peut pas être placé ici selon les règles du Sudoku.") 
                continue
            last_move = (row, col, num)
            confirm = ask_yes_no(f"Confirmer l'entrée {num} en ligne {row+1}, colonne {col+1} ?")   # Ask for confirmation
            if confirm:
                return row, col, num
            else:
                print("Entrée annulée. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer des chiffres valides.")