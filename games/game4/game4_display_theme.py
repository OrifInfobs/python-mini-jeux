"""
Display the theme and shuffled words for Game 4.
"""

from utils.colorama import Fore, Style


def display_theme_and_words(theme, shuffled_words):
    """
    Display the theme and the list of shuffled words.
    Args:
        theme (str): The theme of the round.
        shuffled_words (list[str]): The list of shuffled words.
    """
    print(f"\n{Fore.MAGENTA}Thème : {theme}{Style.RESET_ALL}\n")
    for i, word in enumerate(shuffled_words, 1):
        print(f"{Fore.GREEN}{Style.BRIGHT}{i}.{Style.RESET_ALL} {word}")
