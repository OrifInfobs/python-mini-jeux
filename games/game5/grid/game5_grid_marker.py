def display_grid_with_marker(grid, row=None, col=None):
    # Affiche la grille avec un marqueur sur la case sélectionnée
    for i, ligne in enumerate(grid):
        row_str = ""
        for j, val in enumerate(ligne):
            if i == row and j == col:
                row_str += f"[{val if val != 0 else '.'}] "
            else:
                row_str += f" {val if val != 0 else '.'}  "
        print(f"{i+1} | {row_str}")
    print("    " + "  ".join(str(j+1) for j in range(9)))
