from .game5_check_endgame import check_end_game
from .grid.game5_grid_fill import fill_Grid
# This function is called when the game ends, for Daniel to implement
def end_game(grid):
    check_end_game()
    print("Voici la solution du sudoku :")
    print(fill_Grid(grid))
