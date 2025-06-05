"""
Start the main game loop for Game 4.
"""

from .game4_check_player_guess import check_player_guess
from .game4_select_imposter import select_theme_and_imposter
from .game4_shuffle import shuffle_list
from utils.colorama import Fore, Style
import os


def clear_console():
    """
    Clear the console screen.
    """
    os.system('cls')


def game():
    """
    Main internal game function for Game 4.
    Args:
        bool: True if the player found the imposter, False otherwise.
    """
    while True:
        theme, normal_words, imposter_word = select_theme_and_imposter()
        clear_console()
        print(
            f"Vous avez choisi le thème :{Fore.BLUE}{theme}{Style.RESET_ALL}\n"
        )
        words_with_imposter = normal_words + [imposter_word]
        shuffled_words = shuffle_list(words_with_imposter)
        if check_player_guess(imposter_word, shuffled_words):
            return True
        else:
            return False
