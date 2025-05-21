from games.game5.grid.game5_grid_is_valid import is_valid

def check_end_game(grid):
    for row in range(9):                            # Vérifie que toutes les cases sont remplies et valides
        for col in range(9):
            num = grid[row][col]
            if num == 0:
                return False                        # Grille incomplète
            grid[row][col] = 0                      # On retire temporairement le nombre pour vérifier la validité
            if not is_valid(grid, row, col, num):
                grid[row][col] = num                # Restaure la valeur
                return False                        # Mauvaise solution
            grid[row][col] = num                    # Restaure la valeur
    return True                                     # Grille complète et correcte