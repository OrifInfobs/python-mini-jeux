from games.game5.game5_functions.game5_check_endgame import result
from games.game5.grid.game5_display_grid import display_Grid

def end_game(solution_grid):
    result(solution_grid)
    print("Voici la solution du sudoku :")
    display_Grid(solution_grid)