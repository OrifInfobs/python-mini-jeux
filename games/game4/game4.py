"""
Main logic for Game 4.
"""

from .game4_introduction import introduction
from .game4_game_start import game
import os


def Clear():
    os.system("cls")    # Clear console function


def play():             # Main function when game is called
    Clear()
    introduction()
    return game()
