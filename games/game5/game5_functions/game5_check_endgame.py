from games.game5.grid.game5_grid_is_valid import is_valid

def check_end_game(grid):
    # Vérifie que toutes les cases sont remplies et valides
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num == 0:
                return False  # Grille incomplète
            # On retire temporairement le nombre pour vérifier la validité
            grid[row][col] = 0
            if not is_valid(grid, row, col, num):
                grid[row][col] = num  # Restaure la valeur
                return False  # Mauvaise solution
            grid[row][col] = num  # Restaure la valeur
    return True  # Grille complète et correcte