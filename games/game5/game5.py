"""
Main logic for Game 5 (Sudoku).
"""

from games.game5.game5_functions.game5_intro import introduction
from games.game5.game5_functions.game5_sudoku_game import run_sudoku_game


def play():
    """
    Run the introduction and start the sudoku game.
    """
    introduction()
    return run_sudoku_game()
