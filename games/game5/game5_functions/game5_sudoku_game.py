"""
Sudoku game logic for Game 5.
"""

import copy
from games.game5.game5_functions.game5_is_grid_full import is_grid_full
from games.game5.grid.game5_init_Grid import init_grid
from games.game5.grid.game5_grid_fill import grid_fill
from games.game5.game5_functions.game5_hints import starting_Hints
from games.game5.game5_functions.game5_endgame import end_game
from games.game5.game5_functions.game5_output_utilisateur import user_output
from games.game5.game5_functions.game5_check_endgame import result
from games.game5.game5_functions.game5_select_difficulty import select_difficulty
from games.game5.game5_functions.game5_Zug_Zug import contains_zugzug_date


def run_sudoku_game():
    """
    Main function to run the Sudoku game.
    """
    min_hints, max_hints = select_difficulty()
    grid = init_grid()
    grid_fill(grid)
    solution_grid = copy.deepcopy(grid)
    grid, hint_positions = starting_Hints(grid, min_hints, max_hints)
    player_moves = set()

    while True:
        action = user_output(grid, hint_positions, player_moves)
        if action == "submit":
            if contains_zugzug_date(grid):
                return "zugzug"
            if not is_grid_full(grid):
                print(
                    "La grille n'est pas encore complète. "
                    "Remplissez toutes les cases avant de soumettre."
                )
                continue
            if result(grid) is True:
                print("Félicitations ! Vous avez résolu le Sudoku !")
                return True
            else:
                print("Dommage ! Vous n'avez pas trouvé la solution.")
                end_game(solution_grid)
                return False
