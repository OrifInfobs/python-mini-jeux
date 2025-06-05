"""
Shuffle and display the list of words for Game 4.
"""

import random
from colorama import Fore, Style


def shuffle_list(lst):
    """
    Shuffle a copy of the list and display the words with numbers.

    Args:
        lst (list[str]): The list of words to shuffle.

    Returns:
        list[str]: The shuffled list of words.
    """
    shuffled_list = lst.copy()
    random.shuffle(shuffled_list)
    print("\nChoisissez l'intrus en entrant un numéro (1-4) :")
    for i, word in enumerate(shuffled_list, 1):
        print(f"{i}. {Fore.GREEN}{word}{Style.RESET_ALL}")
    return shuffled_list
