import copy
from games.game5.grid.game5_grid_update import update_Grid
from games.game5.grid.game5_init_Grid import init_Grid
from games.game5.grid.game5_display_grid import display_Grid
from games.game5.grid.game5_grid_fill import grid_fill
from games.game5.game5_functions.game5_hints import starting_Hints
from games.game5.game5_functions.game5_endgame import result
from games.game5.game5_functions.game5_endgame import end_game
from games.game5.game5_functions.game5_output_utilisateur import userOutput
from games.game5.game5_functions.game5_modifications import allow_modification

def run_sudoku_game():
    grid = init_Grid()                    # 1. Initialize grid
    grid_fill(grid)                       # 2. Fill grid with numbers (full solution)
    solution_grid = copy.deepcopy(grid)   # 3. Copy the filled grid to show the solution later
    starting_Hints(grid)                  # 4. Remove numbers, leaving 1-3 per subgrid
    allow_modification()                  # 5. Allow modification of the grid
    while True:

        print(solution_grid)              # Show the solution grid DEBUG

        row, col, num = userOutput(grid)          # 6. Get user input
        if row is not None and col is not None:   # 7. If user input is valid
            if num == solution_grid[row][col]:    # 8. Check if the number is correct based on the solution
                update_Grid(grid, row, col, num)  # 9. Update grid with user input if correct
                display_Grid(grid)                # 10. Display updated grid to the player
            else:
                end_game(solution_grid)   # 11. If user loses show solution
                return False              # 12. End game
        if row is None:                   # 13. If user loses follow the instructions
            end_game(solution_grid)       # 14. Show solution 
            return False                   # 15. End game
        elif result(grid):        # 16. Check if the game is over
            end_game(solution_grid)       # 17. If yes show solution
            return False                  # 18. End game