from .game4_check_player_guess import check_player_guess
from .game4_select_imposter import select_theme_and_imposter
from .game4_shuffle import shuffle_list
from utils.colorama import Fore, Style
import os
Clear = lambda: os.system('cls')

def game():                                                              # Main internal game function
    while True:
        theme, normal_words, imposter_word = select_theme_and_imposter() # Select theme and imposter word
        Clear()                                                          # Clear the console
        print(f" Vous avez choisi le thème : {Fore.BLUE}{theme}{Style.RESET_ALL}\n")  # Theme in blue
        words_with_imposter = normal_words + [imposter_word]             # Combine and shuffle words
        shuffled_words = shuffle_list(words_with_imposter)               # Display shuffled words         
        if check_player_guess(imposter_word, shuffled_words):            # Check player's guess
            return True
        else:
            return False