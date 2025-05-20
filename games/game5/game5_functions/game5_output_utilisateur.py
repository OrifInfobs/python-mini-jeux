from games.game5.grid.game5_grid_is_valid import is_valid
from games.game5.grid.game5_grid_display import display_Grid
from games.game5.grid.game5_grid_marker import display_grid_with_marker

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
    allow_modification = ask_yes_no("Permettre les modifications en cas d'erreur ?")
    last_move = None
    while True:
        print("\nVoici la grille actuelle :")
        display_Grid(grid)
        try:
            row = int(input("Numéro de ligne (1-9) : ")) - 1
            col = int(input("Numéro de colonne (1-9) : ")) - 1
            if not (0 <= row < 9 and 0 <= col < 9):
                print("Veuillez entrer des numéros entre 1 et 9.")
                continue
            display_grid_with_marker(grid, row, col)
            num = int(input("Nombre à placer (1-9) : "))
            if not (1 <= num <= 9):
                print("Veuillez entrer un nombre entre 1 et 9.")
                continue
            if grid[row][col] != 0 and not allow_modification:
                print("Cette case est déjà remplie.")
                continue
            if not is_valid(grid, row, col, num):
                print("Ce nombre ne peut pas être placé ici selon les règles du Sudoku.")
                continue
            last_move = (row, col, num)
            confirm = ask_yes_no(f"Confirmer l'entrée {num} en ligne {row+1}, colonne {col+1} ?")
            if confirm:
                return row, col, num
            else:
                print("Entrée annulée. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer des chiffres valides.")