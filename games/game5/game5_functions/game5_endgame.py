from games.game5.game5_functions.game5_check_endgame import check_end_game
from games.game5.grid.game5_grid_display import display_Grid

def end_game(solution_grid):
    check_end_game(solution_grid)
    print("Voici la solution du sudoku :")
    display_Grid(solution_grid)