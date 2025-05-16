from .grid.game5_grid_update import update_Grid
from .grid.game5_init_Grid import init_Grid
from .grid.game5_grid_display import display_Grid
from .grid.game5_grid_fill import fill_Grid
from .game5_hints import starting_Hints  
from .game5_output_utilisateur import userOutput

def run_sudoku_game():
    grid = init_Grid()           # 1. Initialize grid
    fill_Grid(grid)              # 2. Fill grid with numbers (full solution)
    starting_Hints(grid)         # 3. Remove numbers, leaving 1-3 per subgrid
    display_Grid(grid)           # 4. Display grid to player       
    while True:
        userOutput()             # 6. Display user output
