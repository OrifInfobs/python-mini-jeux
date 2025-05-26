from games.game5.grid.game5_display_grid import display_Grid
from games.game5.game5_functions.game5_yes_no import ask_yes_no

def userOutput(grid):
    while True:
        print("\nVoici la grille actuelle :\n")
        display_Grid(grid)
        print("\n1. Remplir/modifier une case")
        print("\n2. Effacer une case")
        print("\n3. Soumettre la grille")
        choice = input("\nVotre choix (1/2/3) : ").strip()
        if choice == "1":
            try:
                row = int(input("Numéro de ligne (1-9) : ")) - 1
                col = int(input("Numéro de colonne (1-9) : ")) - 1
                num = int(input("Nombre à placer (1-9) : "))
                if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                    grid[row][col] = num
                else:
                    print("Entrée hors limites.")
            except ValueError:
                print("Entrée invalide.")
        elif choice == "2":
            try:
                row = int(input("Numéro de ligne (1-9) à effacer : ")) - 1
                col = int(input("Numéro de colonne (1-9) à effacer : ")) - 1
                if 0 <= row < 9 and 0 <= col < 9:
                    grid[row][col] = 0
                else:
                    print("Entrée hors limites.")
            except ValueError:
                print("Entrée invalide.")
        elif choice == "3":
            confirm = ask_yes_no("Voulez-vous soumettre la grille ?")
            if confirm:
                return "submit"
        else:
            print("Choix invalide.")