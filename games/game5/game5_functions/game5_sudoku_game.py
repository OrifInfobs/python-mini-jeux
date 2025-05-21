import copy
from games.game5.grid.game5_grid_update import update_Grid
from games.game5.grid.game5_init_Grid import init_Grid
from games.game5.grid.game5_display_grid import display_Grid
from games.game5.grid.game5_grid_fill import grid_fill
from games.game5.game5_functions.game5_hints import starting_Hints
from games.game5.game5_functions.game5_endgame import check_end_game
from games.game5.game5_functions.game5_endgame import end_game
from games.game5.game5_functions.game5_output_utilisateur import userOutput

def run_sudoku_game():
    grid = init_Grid()                   # 1. Initialize grid
    grid_fill(grid)                      # 2. Fill grid with numbers (full solution)
    solution_grid = copy.deepcopy(grid)  # 3. Copy the filled grid to show the solution later
    starting_Hints(grid)                 # 4. Remove numbers, leaving 1-3 per subgrid
    while True:
        row, col, num = userOutput(grid)  # 5. Get user input from user_output
        update_Grid(grid, row, col, num)  # 6. Update grid with player input
        display_Grid(grid)                # 7. Display updated grid
        if check_end_game(grid):          # 8. Check if the game is over
            end_game(solution_grid)       # 9. Show the solution
            break